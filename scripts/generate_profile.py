#!/usr/bin/env python3
"""Generate only AUTO regions from one public GitHub/RSS snapshot (stdlib only)."""
from __future__ import annotations

import argparse
import html
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / 'scripts/profile.config.json'
FILES = {'en': ROOT / 'README.md', 'zh': ROOT / 'README_zh.md'}
API = 'https://api.github.com'
TIMEOUT = 30
REGION = re.compile(r'<!-- AUTO:([\w:-]+):START -->.*?<!-- AUTO:\1:END -->', re.S)


def request(url, token=None):
    headers = {'User-Agent': 'profile-readme-generator', 'Accept': 'application/vnd.github+json'}
    if token:
        headers['Authorization'] = f'Bearer {token}'
    for attempt in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=TIMEOUT) as response:
                return response.read()
        except urllib.error.HTTPError as exc:
            if exc.code not in (429, 500, 502, 503, 504) or attempt == 2:
                raise
        except (urllib.error.URLError, TimeoutError):
            if attempt == 2:
                raise
        time.sleep(2 ** attempt)


def api_json(path, token=None, optional=False):
    try:
        return json.loads(request(API + path, token))
    except urllib.error.HTTPError as exc:
        if optional and exc.code == 404:
            return {}
        raise


def pages(path, token=None):
    result = []
    for page in range(1, 1001):
        batch = api_json(f'{path}{"&" if "?" in path else "?"}per_page=100&page={page}', token)
        if not isinstance(batch, list):
            raise ValueError('expected a paginated list')
        result.extend(batch)
        if len(batch) < 100:
            return result
    raise ValueError('pagination safety limit reached')


def safe_url(value):
    value = value.strip()
    parsed = urllib.parse.urlsplit(value)
    if parsed.scheme not in ('https', 'http') or not parsed.netloc or parsed.username or parsed.password:
        raise ValueError(f'unsafe public URL: {value!r}')
    return urllib.parse.quote(value, safe=':/?#@!$&\'*+,;=%-._~')


def esc(value):
    return html.escape(str(value), quote=True)


def md(value):
    return re.sub(r'([\\`*_{}\[\]<>|])', r'\\\1', str(value).replace('\n', ' '))


def parse_posts(raw, count):
    root = ET.fromstring(raw)
    posts, seen = [], set()
    atom = '{http://www.w3.org/2005/Atom}'
    for item in root.findall('.//item') + root.findall(f'{atom}entry'):
        title = (item.findtext('title') or item.findtext(f'{atom}title') or '').strip()
        link = (item.findtext('link') or '').strip()
        if not link:
            link = next((e.get('href', '') for e in item.findall(f'{atom}link') if e.get('rel', 'alternate') == 'alternate'), '')
        link = safe_url(link)
        pub = item.findtext('pubDate') or item.findtext(f'{atom}published') or item.findtext(f'{atom}updated') or ''
        date = ''
        if pub:
            try:
                date = parsedate_to_datetime(pub).astimezone(timezone.utc).date().isoformat()
            except (ValueError, TypeError):
                date = datetime.fromisoformat(pub.replace('Z', '+00:00')).date().isoformat()
        if title and link not in seen:
            posts.append({'title': title, 'url': link, 'date': date})
            seen.add(link)
    posts.sort(key=lambda p: (p['date'], p['url']), reverse=True)
    if not posts:
        raise ValueError('blog feed returned no valid items')
    return posts[:count]


def public_repos(repos, cfg):
    excluded = {n.casefold() for n in cfg.get('exclude_repos', [])}
    owner = cfg['username'].casefold()
    return sorted((r for r in repos if not r.get('private') and r.get('visibility', 'public') == 'public'
                   and r.get('owner', {}).get('login', '').casefold() == owner
                   and r['name'].casefold() not in excluded), key=lambda r: r['name'].casefold())


def recent_repos(repos, cfg):
    excluded = {n.casefold() for n in cfg.get('now', {}).get('exclude', [])}
    return sorted((r for r in repos if not r.get('fork') and not r.get('archived') and r.get('pushed_at')
                   and r['name'].casefold() not in excluded),
                  key=lambda r: (r['pushed_at'], r['name']), reverse=True)[:cfg['now']['count']]


def collect(cfg, token=None):
    # Do not use /user/repos: it can disclose private repositories with a PAT.
    repos = public_repos(pages(f"/users/{cfg['username']}/repos?type=owner", token), cfg)
    if not repos:
        raise ValueError('public repository list unexpectedly empty; refusing destructive refresh')
    user = api_json(f"/users/{cfg['username']}", token)
    names = {r['name'] for r in recent_repos(repos, cfg)}
    names.update(n for section in cfg['sections'] for n in section['repos'])
    available = {r['name'] for r in repos}
    releases = {name: api_json(f"/repos/{cfg['username']}/{name}/releases/latest", token, optional=True)
                for name in sorted(names & available)}
    maintenance = {}
    for name in cfg.get('maintenance', {}).get('repos', []):
        if name not in available:
            continue
        # Public, recently updated closed PRs; explicitly not an exhaustive PR history.
        prs = api_json(f"/repos/{cfg['username']}/{name}/pulls?state=closed&sort=updated&direction=desc&per_page=100", token)
        maintenance[name] = sorted((p for p in prs if p.get('merged_at')),
                                   key=lambda p: p['merged_at'], reverse=True)[:cfg['maintenance']['count']]
    try:
        posts = parse_posts(request(cfg['blog']['feed']), cfg['posts']['count'])
        feed_error = None
    except Exception as exc:
        posts, feed_error = None, str(exc)
        print(f'warning: RSS unavailable; preserving POSTS in both languages: {exc}', file=sys.stderr)
    return {'repos': repos, 'user': {'followers': user['followers']}, 'releases': releases,
            'maintenance': maintenance, 'posts': posts, 'feed_error': feed_error}


def pick_desc(repo, lang, cfg):
    # Only explicitly curated, timeless translations belong in this map.
    return (cfg.get('descriptions', {}).get(repo['name'], {}).get(lang) or repo.get('description') or '').strip()


def derive_type(repo, lang, cfg):
    topics = {t.lower() for t in repo.get('topics', [])}
    labels = [rule[lang] for rule in cfg.get('type_labels', []) if topics & set(rule['topics'])][:cfg.get('max_type_labels', 2)]
    if repo.get('language'):
        labels.append(repo['language'])
    return ' · '.join(labels)


def render_cards(names, lang, cfg, data):
    by_name = {r['name']: r for r in data['repos']}
    cells = []
    for name in names:
        if name not in by_name:
            print(f'notice: skipping unavailable public repository {name}', file=sys.stderr)
            continue
        repo = by_name[name]
        release = data['releases'].get(name, {})
        tag = f" · {release['tag_name']}" if release.get('tag_name') else ''
        stars = f" · ★ {repo['stargazers_count']}" if repo.get('stargazers_count') else ''
        archived = (' · Archived' if lang == 'en' else ' · 已归档') if repo.get('archived') else ''
        cells.append('<td width="50%" valign="top">\n'
                     f'<a href="{esc(safe_url(repo["html_url"]))}"><b>{esc(name)}</b></a><br>\n'
                     f'<sub>{esc(derive_type(repo, lang, cfg) + stars + tag + archived)}</sub><br><br>\n'
                     f'{esc(pick_desc(repo, lang, cfg))}\n</td>')
    if not cells:
        return 'No public repositories in this group.' if lang == 'en' else '此分组暂无公开仓库。'
    if len(cells) % 2:
        cells.append('<td width="50%"></td>')
    return '<table>\n' + '\n'.join('<tr>\n' + '\n'.join(cells[i:i+2]) + '\n</tr>' for i in range(0, len(cells), 2)) + '\n</table>'


def render_now(cfg, lang, data):
    lines = []
    for repo in recent_repos(data['repos'], cfg):
        release = data['releases'].get(repo['name'], {})
        tag = f" · {md(release['tag_name'])}" if release.get('tag_name') else ''
        # Absolute UTC timestamps do not become misleading between scheduled runs.
        label = 'pushed' if lang == 'en' else '推送于'
        lines.append(f"- **[{md(repo['name'])}]({safe_url(repo['html_url'])})**{tag} — {md(pick_desc(repo, lang, cfg))} · {label} {repo['pushed_at'].replace('T', ' ').replace('Z', ' UTC')}")
    return '\n'.join(lines) or ('No recent public activity.' if lang == 'en' else '暂无公开动态。')


def render_stats(cfg, lang, data):
    repos = data['repos']
    own = [r for r in repos if not r.get('fork')]
    counts = Counter(r['language'] for r in own if r.get('language'))
    values = [len(repos), len(own), sum(r.get('stargazers_count', 0) for r in own),
              sum(r.get('forks_count', 0) for r in own), data['user']['followers']]
    labels = (['Public repositories', 'Non-fork repositories', 'Stars (non-fork)', 'Forks received (non-fork)', 'Followers'] if lang == 'en'
              else ['公开仓库', '非 Fork 仓库', '获星数（非 Fork）', '被 Fork 数（非 Fork）', '关注者'])
    lines = [f'- {label}: **{value}**' for label, value in zip(labels, values)]
    languages = ', '.join(f'{md(name)} ({count})' for name, count in sorted(counts.items(), key=lambda p: (-p[1], p[0]))[:6])
    lines.append(('- Primary languages by non-fork repository count: ' if lang == 'en' else '- 按非 Fork 仓库数量统计的主要语言：') + (languages or '—'))
    lines.append(('_Source: public GitHub API; excludes private data. Language counts are not code-byte percentages._' if lang == 'en'
                  else '_来源：GitHub 公开 API，不含私有数据；语言按仓库计数，不代表代码字节占比。_'))
    return '\n'.join(lines)


def render_catalog(cfg, lang, data):
    featured = {n for s in cfg['sections'] for n in s['repos']}
    return '\n'.join(f"- [{md(r['name'])}]({safe_url(r['html_url'])})" +
                     (f" — {md(pick_desc(r, lang, cfg))}" if pick_desc(r, lang, cfg) else '')
                     for r in data['repos'] if not r.get('fork') and r['name'] not in featured and r['name'] != cfg['username']) or '—'


def render_maintenance(cfg, lang, data):
    lines = []
    for name, prs in sorted(data['maintenance'].items()):
        for pr in prs:
            lines.append(f"- [{md(name)} #{pr['number']}]({safe_url(pr['html_url'])}) — {md(pr['title'])} · {pr['merged_at'][:10]}")
    label = ('Recently merged PRs among the 100 most recently updated closed PRs per configured repository:' if lang == 'en'
             else '配置仓库最近更新的 100 条已关闭 PR 中，最近合并的记录：')
    return label + '\n\n' + ('\n'.join(lines) or ('No merged PRs found.' if lang == 'en' else '暂无已合并 PR。'))


def replace_region(text, key, body):
    start, end = f'<!-- AUTO:{key}:START -->', f'<!-- AUTO:{key}:END -->'
    if text.count(start) != 1 or text.count(end) != 1 or text.index(start) >= text.index(end):
        raise ValueError(f'missing, duplicated or reversed markers for {key}')
    return re.sub(re.escape(start) + r'.*?' + re.escape(end), lambda _: f'{start}\n{body.rstrip()}\n{end}', text, flags=re.S)


def manual_text(text):
    return REGION.sub(lambda m: f'<!-- AUTO:{m[1]} -->', text)


def generate(texts, cfg, data):
    data = dict(data, repos=public_repos(data['repos'], cfg))
    output = {}
    for lang, original in texts.items():
        text = original
        bodies = {f"CARDS:{s['id']}": render_cards(s['repos'], lang, cfg, data) for s in cfg['sections']}
        bodies.update(NOW=render_now(cfg, lang, data), STATS=render_stats(cfg, lang, data),
                      CATALOG=render_catalog(cfg, lang, data), MAINTENANCE=render_maintenance(cfg, lang, data))
        if data['posts'] is not None:
            bodies['POSTS'] = '\n'.join(f"- [{md(p['title'])}]({safe_url(p['url'])})" + (f" — {p['date']}" if p['date'] else '') for p in data['posts'])
        for key, body in bodies.items():
            text = replace_region(text, key, body)
        if manual_text(original) != manual_text(text):
            raise ValueError('manual content changed')
        output[lang] = text
    validate(output, cfg, data)
    return output


def validate(texts, cfg, data):
    expected = {f"CARDS:{s['id']}" for s in cfg['sections']} | {'NOW', 'POSTS', 'STATS', 'CATALOG', 'MAINTENANCE'}
    refs = {}
    for lang, text in texts.items():
        keys = re.findall(r'<!-- AUTO:(.*?):START -->', text)
        ends = re.findall(r'<!-- AUTO:(.*?):END -->', text)
        if set(keys) != expected or set(ends) != expected or len(keys) != len(expected) or len(ends) != len(expected):
            raise ValueError(f'{lang}: unexpected AUTO marker inventory')
        bodies = {m[1]: m[0] for m in REGION.finditer(text)}
        if set(bodies) != expected:
            raise ValueError(f'{lang}: invalid AUTO marker ordering')
        refs[lang] = {key: re.findall(r'(?:href="|\]\()(https?[^"\s)]+)', body) for key, body in bodies.items()}
        for key in expected:
            for excluded in cfg.get('exclude_repos', []):
                if re.search(r'https://github\.com/' + re.escape(cfg['username'] + '/' + excluded) + r'(?:["/)\s]|$)', bodies[key], re.I):
                    raise ValueError(f'excluded repository leaked into {key}')
    if refs.get('en') != refs.get('zh'):
        raise ValueError('bilingual AUTO references differ')
    return {lang: {key: len(urls) for key, urls in sections.items()} for lang, sections in refs.items()}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--snapshot-in', type=Path)
    parser.add_argument('--snapshot-out', type=Path)
    parser.add_argument('--check', action='store_true', help='render without writes; fail if output differs')
    parser.add_argument('--report', type=Path)
    args = parser.parse_args(argv)
    cfg = json.loads(CONFIG_PATH.read_text())
    data = json.loads(args.snapshot_in.read_text()) if args.snapshot_in else collect(cfg, os.environ.get('GITHUB_TOKEN'))
    if args.snapshot_out:
        args.snapshot_out.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    originals = {lang: path.read_text() for lang, path in FILES.items()}
    output = generate(originals, cfg, data)
    if generate(output, cfg, data) != output:
        raise ValueError('generation is not idempotent')
    report = {'references': validate(output, cfg, data), 'idempotent': True, 'manual_content_unchanged': True,
              'rss_preserved': data['posts'] is None, 'public_repositories': len(public_repos(data['repos'], cfg))}
    if args.report:
        args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(report, ensure_ascii=False))
    if args.check:
        return int(output != originals)
    # All network operations, rendering and validation finish before either file is written.
    for lang, path in FILES.items():
        path.write_text(output[lang])
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
