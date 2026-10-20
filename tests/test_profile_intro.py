import json
import re
import sys
import unittest
import urllib.parse
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import generate_profile as gp
from test_generate_profile import config, data, repo, texts

CONFIG = json.loads((ROOT / "scripts/profile.config.json").read_text(encoding="utf-8"))
READMES = ("README.md", "README_zh.md")
DELETED_REPO = "xinvxueyuan.github.io"
RETIRED_QUOTE = "交配仪式"
EXTRA_REGIONS = ("BLOG", "BLOG_BADGE", "STATS_IMAGES")


def readme(name):
    return (ROOT / name).read_text(encoding="utf-8")


def host_of(url):
    return (urllib.parse.urlsplit(url).hostname or "").removeprefix("www.")


class ProfileIntroTests(unittest.TestCase):
    def test_section_markers_match_the_configured_sections(self):
        expected = {f"CARDS:{section['id']}" for section in CONFIG["sections"]}
        for name in READMES:
            text = readme(name)
            self.assertEqual(expected, set(re.findall(r"<!-- AUTO:(CARDS:[\w-]+):START -->", text)))
            self.assertEqual(expected, set(re.findall(r"<!-- AUTO:(CARDS:[\w-]+):END -->", text)))

    def test_generated_region_inventory_is_complete_and_unique(self):
        expected = ({f"CARDS:{section['id']}" for section in CONFIG["sections"]}
                    | {"NOW", "POSTS", "STATS", "CATALOG", "MAINTENANCE", *EXTRA_REGIONS})
        for name in READMES:
            starts = re.findall(r"<!-- AUTO:(.*?):START -->", readme(name))
            self.assertEqual(len(expected), len(starts))
            self.assertEqual(expected, set(starts))

    def test_section_ids_are_unique_and_non_empty(self):
        ids = [section["id"] for section in CONFIG["sections"]]
        self.assertEqual(len(ids), len(set(ids)))
        for section in CONFIG["sections"]:
            self.assertTrue(section["repos"], section["id"])

    def test_generated_output_carries_the_configured_site_urls(self):
        url, feed, stats = CONFIG["blog"]["url"], CONFIG["blog"]["feed"], CONFIG["stats"]["base"]
        host = host_of(url)
        self.assertTrue(host)
        for name in READMES:
            text = readme(name)
            self.assertIn(f"]({url})", text)
            self.assertIn(f"]({feed})", text)
            self.assertIn(stats, text)
            self.assertIn(host, text)

    def test_hand_written_text_has_no_site_domain_literals(self):
        hosts = {host_of(CONFIG["blog"]["url"]),
                 urllib.parse.urlsplit(CONFIG["stats"]["base"]).hostname or ""}
        for name in READMES:
            manual = gp.manual_text(readme(name))
            for host in hosts:
                self.assertTrue(host)
                self.assertNotIn(host, manual, f"{name} hand-written text mentions {host}")

    def test_intro_mentions_the_work_and_drops_the_old_signature(self):
        for name in READMES:
            text = readme(name)
            self.assertNotIn("AUTO:BIO", text)
            self.assertNotIn(RETIRED_QUOTE, text)
            intro = re.split(r"^---$", text, maxsplit=1, flags=re.M)[0]
            for topic in ("MCP", "Cordis", "NoneBot2"):
                self.assertIn(topic, intro)

    def test_deleted_site_repository_is_referenced_nowhere(self):
        self.assertNotIn(DELETED_REPO, (ROOT / "scripts/profile.config.json").read_text(encoding="utf-8"))
        for name in READMES:
            self.assertNotIn(DELETED_REPO, readme(name))

    def test_generator_rejects_a_readme_that_still_has_a_bio_region(self):
        original = texts()
        original["en"] = original["en"].replace(
            "manual after",
            "<!-- AUTO:BIO:START -->\n> *Old signature*\n<!-- AUTO:BIO:END -->\nmanual after",
        )
        with self.assertRaises(ValueError):
            gp.generate(original, config(), data([]))

    def test_generation_preserves_a_hand_written_introduction(self):
        original = texts()
        intro = "# Title\n\nA hand-written introduction without links.\n\n"
        for lang in original:
            original[lang] = intro + original[lang]
        output = gp.generate(original, config(), data([]))
        for lang in output:
            self.assertTrue(output[lang].startswith(intro))
            self.assertIn("manual after", output[lang])

    def test_collect_reads_followers_without_copying_the_profile_bio(self):
        cfg = config()
        calls = []

        def api(path, token=None, optional=False):
            calls.append(path)
            if path == "/users/alice":
                return {"followers": 9, "bio": "This text must never reach a README."}
            return {}

        with patch.object(gp, "pages", return_value=[repo("good")]), \
             patch.object(gp, "api_json", side_effect=api), \
             patch.object(gp, "request", return_value=b"<rss/>"), \
             patch.object(gp, "parse_posts", return_value=[]):
            snapshot = gp.collect(cfg)

        self.assertEqual({"followers": 9}, snapshot["user"])
        self.assertEqual(1, sum(path.startswith("/users/") for path in calls))
        self.assertNotIn("This text must never reach a README.", json.dumps(snapshot))


if __name__ == "__main__":
    unittest.main()
