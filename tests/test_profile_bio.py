import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import generate_profile as gp
from test_generate_profile import config, data, repo, texts


class ProfileBioTests(unittest.TestCase):
    def test_collect_fetches_followers_and_bio_from_shared_user_snapshot(self):
        cfg = config()
        repositories = [repo("good"), repo("other")]
        api_calls = []

        def api(path, token=None, optional=False):
            api_calls.append(path)
            if path == "/users/alice":
                return {"followers": 12, "bio": "  Building useful tools.  "}
            return {}

        with patch.object(gp, "pages", return_value=repositories), \
             patch.object(gp, "api_json", side_effect=api), \
             patch.object(gp, "request", return_value=b"<rss/>"), \
             patch.object(gp, "parse_posts", return_value=[]):
            snapshot = gp.collect(cfg)

        self.assertEqual({"followers": 12, "bio": "  Building useful tools.  "}, snapshot["user"])
        self.assertEqual(1, api_calls.count("/users/alice"))
        self.assertEqual(1, sum(path.startswith("/users/") for path in api_calls))

    def test_render_bio_normalizes_whitespace_and_escapes_html_markdown_and_auto_text(self):
        bio = "  <b>A & *bio*</b>\n\t<!-- AUTO:BIO:START -->  "
        normalized = "<b>A & *bio*</b> <!-- AUTO:BIO:START -->"
        expected = "> *" + gp.md(gp.esc(normalized)) + "*"

        self.assertEqual(expected, gp.render_bio({"user": {"bio": bio}}))
        self.assertIn("&lt;b&gt;", expected)
        self.assertIn("&amp;", expected)
        self.assertIn(r"\*bio\*", expected)
        self.assertIn("&lt;!-- AUTO:BIO:START --&gt;", expected)
        self.assertNotIn("\n", expected)

    def test_nonempty_bio_is_bilingual_idempotent_and_preserves_manual_text(self):
        cfg = config()
        payload = data([])
        payload["user"] = {"followers": 7, "bio": "  Build *things*\nwith care.  "}
        original = texts()

        output = gp.generate(original, cfg, payload)
        self.assertEqual(output, gp.generate(output, cfg, payload))
        expected = gp.render_bio(payload)
        for lang in ("en", "zh"):
            self.assertEqual(1, output[lang].count("<!-- AUTO:BIO:START -->"))
            self.assertEqual(1, output[lang].count("<!-- AUTO:BIO:END -->"))
            self.assertIn(expected, output[lang])
            self.assertEqual(1, output[lang].count(expected))
            self.assertEqual(gp.manual_text(original[lang]), gp.manual_text(output[lang]))
            self.assertEqual(1, output[lang].count(expected))

    def test_none_empty_whitespace_and_missing_bio_preserve_previous_signature(self):
        cfg = config()
        original = texts()
        for bio in (None, "", " \t\n "):
            payload = data([])
            payload["user"] = {"followers": 7, "bio": bio}
            output = gp.generate(original, cfg, payload)
            for lang in ("en", "zh"):
                self.assertIn("> *Previous signature*", output[lang])
                self.assertNotIn("\n> **", output[lang])
        payload = data([])
        payload["user"] = {"followers": 7}
        output = gp.generate(original, cfg, payload)
        for lang in ("en", "zh"):
            self.assertIn("> *Previous signature*", output[lang])

    def test_old_snapshot_without_bio_remains_compatible(self):
        cfg = config()
        snapshot = data([])
        self.assertNotIn("bio", snapshot["user"])
        output = gp.generate(texts(), cfg, snapshot)
        for lang in ("en", "zh"):
            self.assertIn("> *Previous signature*", output[lang])
            self.assertEqual(1, output[lang].count("<!-- AUTO:BIO:START -->"))
            self.assertEqual(1, output[lang].count("<!-- AUTO:BIO:END -->"))

    def test_duplicate_or_missing_bio_marker_fails_even_when_bio_is_empty(self):
        cfg = config()
        payload = data([])
        payload["user"] = {"followers": 7, "bio": ""}
        original = texts()
        cases = (
            original["en"].replace("<!-- AUTO:BIO:START -->", "<!-- AUTO:BIO:START -->\n<!-- AUTO:BIO:START -->"),
            original["en"].replace("<!-- AUTO:BIO:END -->", ""),
        )
        for malformed in cases:
            with self.subTest(malformed=malformed):
                bad_texts = dict(original)
                bad_texts["en"] = malformed
                with self.assertRaises(ValueError):
                    gp.generate(bad_texts, cfg, payload)

    def test_validate_requires_one_bilingual_bio_region_and_rejects_tampering(self):
        cfg = config()
        payload = data([])
        payload["user"] = {"followers": 7, "bio": "A public signature"}
        output = gp.generate(texts(), cfg, payload)
        report = gp.validate(output, cfg, payload)
        self.assertEqual(report["en"]["BIO"], report["zh"]["BIO"])
        for lang in ("en", "zh"):
            self.assertEqual(1, output[lang].count(gp.render_bio(payload)))

        tampered = dict(output)
        tampered["en"] = output["en"].replace(gp.render_bio(payload), "> *Tampered signature*")
        with self.assertRaises(ValueError):
            gp.validate(tampered, cfg, payload)

    def test_validate_rejects_bilingual_bio_body_mismatch(self):
        cfg = config()
        payload = data([])
        payload["user"] = {"followers": 7, "bio": "A public signature"}
        output = gp.generate(texts(), cfg, payload)
        tampered = dict(output)
        tampered["zh"] = output["zh"].replace(gp.render_bio(payload), "> *另一个签名*")
        with self.assertRaises(ValueError):
            gp.validate(tampered, cfg, payload)


if __name__ == "__main__":
    unittest.main()
