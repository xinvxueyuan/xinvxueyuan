import json
import sys
import unittest
import urllib.error
from io import BytesIO
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import generate_profile as gp


class FakeResponse:
    def __init__(self, data):
        self.data = data
    def __enter__(self):
        return self
    def __exit__(self, *args):
        return False
    def read(self):
        return self.data


def repo(name, **kwargs):
    value = {
        "name": name, "owner": {"login": "alice"}, "private": False,
        "visibility": "public", "fork": False, "archived": False,
        "pushed_at": "2025-01-02T03:04:05Z", "html_url": f"https://github.com/alice/{name}",
        "description": f"{name} description", "language": "Python",
        "topics": [], "stargazers_count": 1, "forks_count": 2,
    }
    value.update(kwargs)
    return value


def config():
    return {
        "username": "alice", "exclude_repos": ["Secret"],
        "sections": [{"id": "FEATURED", "repos": ["good", "gone"]}],
        "now": {"count": 2, "exclude": []}, "posts": {"count": 3},
        "maintenance": {"repos": [], "count": 2}, "descriptions": {},
        "type_labels": [], "max_type_labels": 2,
        "blog": {"feed": "https://example.com/feed.xml"},
    }


def texts():
    keys = ["CARDS:FEATURED", "NOW", "POSTS", "STATS", "CATALOG", "MAINTENANCE"]
    return {lang: "manual before\n" + "\n".join(
        f"<!-- AUTO:{key}:START -->\nold {lang} {key}\n<!-- AUTO:{key}:END -->" for key in keys
    ) + "\nmanual after" for lang in ("en", "zh")}


def data(posts=None):
    return {"repos": [repo("good"), repo("other")], "user": {"followers": 7},
            "releases": {}, "maintenance": {}, "posts": posts if posts is not None else [], "feed_error": None}


class ProfileRegressionTests(unittest.TestCase):
    def test_public_repos_filters_private_nonowner_and_denylist(self):
        items = [repo("good"), repo("Private", private=True), repo("Secret"),
                 repo("OtherOwner", owner={"login": "bob"}), repo("Hidden", visibility="private")]
        self.assertEqual(["good"], [r["name"] for r in gp.public_repos(items, config())])

    def test_pages_handles_more_than_one_hundred(self):
        batches = [[repo(f"r{i}") for i in range(100)], [repo("last")], []]
        with patch.object(gp, "api_json", side_effect=batches) as mocked:
            result = gp.pages("/users/alice/repos")
        self.assertEqual(101, len(result))
        self.assertEqual(2, mocked.call_count)
        self.assertIn("page=2", mocked.call_args_list[1].args[0])

    def test_recent_repos_excludes_fork_archived_and_profile(self):
        cfg = config(); cfg["username"] = "profile"
        items = [repo("new", pushed_at="2025-03-01T00:00:00Z"),
                 repo("fork", fork=True, pushed_at="2025-04-01T00:00:00Z"),
                 repo("arch", archived=True, pushed_at="2025-05-01T00:00:00Z"),
                 repo("profile", pushed_at="2025-06-01T00:00:00Z"),
                 repo("old", pushed_at="2024-01-01T00:00:00Z")]
        cfg["now"]["exclude"] = ["profile"]
        self.assertEqual(["new", "old"], [r["name"] for r in gp.recent_repos(items, cfg)])

    def test_bilingual_idempotent_manual_protection_and_deleted_repo_skip(self):
        cfg = config(); original = texts()
        out = gp.generate(original, cfg, data([{"title": "Post", "url": "https://example.com/p", "date": "2025-01-01"}]))
        self.assertEqual(out, gp.generate(out, cfg, data([{"title": "Post", "url": "https://example.com/p", "date": "2025-01-01"}])))
        for lang in out:
            self.assertIn("manual before", out[lang]); self.assertIn("manual after", out[lang])
            self.assertNotIn("gone description", out[lang])
        self.assertEqual(gp.validate(out, cfg, data([]))["en"], gp.validate(out, cfg, data([]))["zh"])

    def test_rss_failure_preserves_posts_in_both_languages(self):
        cfg = config(); original = texts()
        payload = {"repos": [repo("good")], "user": {"followers": 1}, "releases": {},
                   "maintenance": {}, "posts": None, "feed_error": "offline"}
        out = gp.generate(original, cfg, payload)
        self.assertIn("old en POSTS", out["en"])
        self.assertIn("old zh POSTS", out["zh"])

    def test_collect_rss_failure_is_non_destructive(self):
        cfg = config(); rs = [repo("good")]
        def api(path, token=None, optional=False):
            if path.startswith("/users/"): return {"followers": 3}
            return {}
        with patch.object(gp, "pages", return_value=rs), patch.object(gp, "api_json", side_effect=api), \
             patch.object(gp, "request", side_effect=OSError("feed down")):
            result = gp.collect(cfg)
        self.assertIsNone(result["posts"]); self.assertIn("feed down", result["feed_error"])

    def test_empty_rss_raises_value_error(self):
        with self.assertRaises(ValueError):
            gp.parse_posts(b"<rss><channel></channel></rss>", 5)

    def test_rss_atom_dates_sorting_dedup_and_url_safety(self):
        raw = b'''<feed xmlns="http://www.w3.org/2005/Atom">
          <entry><title>Old</title><link href="https://example.com/old"/><updated>2024-01-01T00:00:00Z</updated></entry>
          <entry><title>New &amp; Safe</title><link rel="alternate" href="https://example.com/new?a=1&amp;b=2"/><published>2025-02-01T00:00:00Z</published></entry>
          <entry><title>Duplicate</title><link href="https://example.com/new?a=1&amp;b=2"/><updated>2026-01-01T00:00:00Z</updated></entry>
        </feed>'''
        posts = gp.parse_posts(raw, 5)
        self.assertEqual(["2025-02-01", "2024-01-01"], [p["date"] for p in posts])
        self.assertEqual("https://example.com/new?a=1&b=2", posts[0]["url"])
        self.assertEqual("New & Safe", posts[0]["title"])

    def test_unsafe_rss_url_is_rejected(self):
        with self.assertRaises(ValueError):
            gp.parse_posts(b'<rss><channel><item><title>x</title><link>javascript:alert(1)</link></item></channel></rss>', 5)

    def test_rendering_escapes_html_and_markdown_and_safe_urls(self):
        cfg = config(); r = repo("<bad>", html_url="https://example.com/a?x=1&y=2", description="<script>x</script>")
        body = gp.render_cards(["<bad>"], "en", cfg, {"repos": [r], "releases": {}})
        self.assertIn("&lt;bad&gt;", body); self.assertIn("&lt;script&gt;", body); self.assertIn("&amp;", body)
        now = gp.render_now(cfg, "en", {"repos": [r], "releases": {}})
        self.assertIn("\\<bad\\>", now)

    def test_marker_duplicate_missing_and_reversed_fail(self):
        original = texts()["en"]
        for bad in (original.replace("<!-- AUTO:NOW:START -->", "<!-- AUTO:NOW:START -->\n<!-- AUTO:NOW:START -->"),
                    original.replace("<!-- AUTO:NOW:END -->", ""),
                    original.replace("<!-- AUTO:NOW:START -->", "X<!-- AUTO:NOW:START -->").replace("<!-- AUTO:NOW:END -->", "<!-- AUTO:NOW:START -->")):
            with self.assertRaises(ValueError): gp.replace_region(bad, "NOW", "body")

    def test_http_403_is_not_swallowed(self):
        error = urllib.error.HTTPError("https://api.github.com", 403, "forbidden", {}, BytesIO(b"no"))
        with patch.object(gp.urllib.request, "urlopen", side_effect=error):
            with self.assertRaises(urllib.error.HTTPError): gp.request("https://api.github.com/nope")

    def test_api_json_and_network_are_mocked_without_external_requests(self):
        with patch.object(gp.urllib.request, "urlopen", return_value=FakeResponse(b'{"ok": true}')):
            self.assertEqual({"ok": True}, gp.api_json("/x"))


if __name__ == "__main__":
    unittest.main()
