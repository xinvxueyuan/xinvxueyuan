#!/usr/bin/env python3
"""Fill the auto-managed regions of the GitHub profile READMEs.

Everything between `<!-- AUTO:<key>:START -->` and `<!-- AUTO:<key>:END -->` is
generated here; everything outside those markers is hand-written and never
touched. Data comes from the GitHub REST API and the blog's RSS feed.

Usage:  GITHUB_TOKEN=... python scripts/generate_profile.py
"""
from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = Path(__file__).resolve().parent / "profile.config.json"
FILES = {"en": ROOT / "README.md", "zh": ROOT / "README_zh.md"}
API = "https://api.github.com"
TIMEOUT = 30

# ---------------------------------------------------------------- HTTP helpers

def _request(url: str, token: str | None = None, accept: str | None = None) -> bytes:
    headers = {"User-Agent": "profile-readme-generator", "Accept": accept or "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return resp.read()


def api_json(path: str, token: str | None) -> dict:
    """GET a GitHub REST path. Returns {} on 404 (e.g. no release yet)."""
    try:
        return json.loads(_request(API + path, token).decode("utf-8"))
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return {}
        raise


# ------------------------------------------------------------------- rendering

def pick_desc(repo: dict, lang: str, cfg: dict) -> str:
    """Per-language override first, then the repository description."""
    override = cfg.get("descriptions", {}).get(repo["name"], {})
    return (override.get(lang) or repo.get("description") or "").strip()


def derive_type(repo: dict, lang: str, cfg: dict) -> str:
    """Card subtitle: labels derived from topics, then the primary language."""
    topics = {t.lower() for t in (repo.get("topics") or [])}
    labels: list[str] = []
    for rule in cfg.get("type_labels", []):
        if topics & set(rule["topics"]):
            labels.append(rule[lang])
            if len(labels) >= cfg.get("max_type_labels", 2):
                break
    if repo.get("language"):
        labels.append(repo["language"])
    return " · ".join(labels)


def render_cards(repo_names: list[str], lang: str, cfg: dict, token: str | None) -> str:
    cells = []
    for name in repo_names:
        repo = api_json(f"/repos/{cfg['username']}/{name}", token)
        if not repo:
            raise SystemExit(f"cannot read repo {cfg['username']}/{name}")
        stars = repo.get("stargazers_count") or 0
        star_txt = f" · ★ {stars}" if stars >= 1 else ""
        cells.append(
            '<td width="50%" valign="top">\n'
            f'<a href="{repo["html_url"]}"><b>{repo["name"]}</b></a><br>\n'
            f'<sub>{derive_type(repo, lang, cfg)}{star_txt}</sub><br><br>\n'
            f'{pick_desc(repo, lang, cfg)}\n'
            "</td>"
        )
    if len(cells) % 2:
        cells.append('<td width="50%"></td>')
    rows = ["<tr>\n" + "\n".join(cells[i:i + 2]) + "\n</tr>" for i in range(0, len(cells), 2)]
    return "<table>\n" + "\n".join(rows) + "\n</table>"


def humanize(iso: str, lang: str) -> str:
    moment = datetime.fromisoformat(iso.replace("Z", "+00:00"))
    seconds = (datetime.now(timezone.utc) - moment).total_seconds()
    if seconds < 3600:
        n, unit = max(1, int(seconds // 60)), "minute"
    elif seconds < 86400:
        n, unit = int(seconds // 3600), "hour"
    elif seconds < 86400 * 30:
        n, unit = int(seconds // 86400), "day"
    elif seconds < 86400 * 365:
        n, unit = int(seconds // (86400 * 30)), "month"
    else:
        n, unit = int(seconds // (86400 * 365)), "year"
    if lang == "zh":
        return f"{n} { {'minute': '分钟前', 'hour': '小时前', 'day': '天前', 'month': '个月前', 'year': '年前'}[unit] }"
    return f"{n} {unit}{'s' if n > 1 else ''} ago"


def render_now(cfg: dict, lang: str, token: str | None) -> str:
    """The most recently pushed non-fork repos owned by the user."""
    own = api_json(f"/users/{cfg['username']}/repos?per_page=100&sort=pushed", token)
    exclude = set(cfg.get("now", {}).get("exclude", []))
    own = [r for r in own if not r.get("fork") and r["name"] not in exclude]
    own.sort(key=lambda r: r.get("pushed_at") or "", reverse=True)
    lines = []
    for repo in own[: cfg.get("now", {}).get("count", 3)]:
        release = api_json(f"/repos/{cfg['username']}/{repo['name']}/releases/latest", token)
        tag = f" `{release['tag_name']}`" if release.get("tag_name") else ""
        desc = pick_desc(repo, lang, cfg)
        suffix = f" — {desc}" if desc else ""
        lines.append(
            f"- 🚀 **[{repo['name']}]({repo['html_url']})**{tag}{suffix} · _{humanize(repo['pushed_at'], lang)}_"
        )
    return "\n".join(lines)


def render_posts(cfg: dict, lang: str) -> str:
    raw = _request(cfg["blog"]["feed"]).decode("utf-8", "replace")
    root = ET.fromstring(raw)
    lines = []
    for item in root.findall(".//item")[: cfg.get("posts", {}).get("count", 5)]:
        title = (item.findtext("title") or "").strip()
        link = (item.findtext("link") or "").strip()
        pub = (item.findtext("pubDate") or "").strip()
        date = ""
        if pub:
            try:
                date = datetime.strptime(pub[:25].strip(), "%a, %d %b %Y %H:%M:%S").strftime("%Y-%m-%d")
            except ValueError:
                date = pub[:16]
        suffix = f" — {date}" if date else ""
        lines.append(f"- [{title}]({link}){suffix}")
    if not lines:
        raise SystemExit("blog feed returned no items")
    return "\n".join(lines)


def replace_region(text: str, key: str, body: str) -> str:
    start, end = f"<!-- AUTO:{key}:START -->", f"<!-- AUTO:{key}:END -->"
    if start not in text or end not in text:
        raise SystemExit(f"missing marker pair for '{key}'")
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.S)
    return pattern.sub(lambda _: f"{start}\n{body.rstrip()}\n{end}", text, count=1)


# ------------------------------------------------------------------------ main

def main() -> int:
    cfg = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    token = os.environ.get("GITHUB_TOKEN")

    for lang, path in FILES.items():
        text = path.read_text(encoding="utf-8")
        for section in cfg["sections"]:
            key = f"CARDS:{section['id']}"
            text = replace_region(text, key, render_cards(section["repos"], lang, cfg, token))
        text = replace_region(text, "NOW", render_now(cfg, lang, token))
        try:
            posts = render_posts(cfg, lang)
        except Exception as exc:  # keep the previous list if the blog is down
            print(f"warning: feed unavailable ({exc}); leaving POSTS untouched", file=sys.stderr)
        else:
            text = replace_region(text, "POSTS", posts)
        path.write_text(text, encoding="utf-8")
        print(f"updated {path.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
