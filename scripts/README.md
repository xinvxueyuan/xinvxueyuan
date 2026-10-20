# Profile automation

The English and Chinese profiles share one public GitHub/RSS snapshot. Only named `AUTO` regions are regenerated. The standard-library-only generator supports Python 3.12 and later; the workflow installs nothing, and `python -S` runs the test suite without site-packages, so there is no `pip` or `setuptools` step. No additional secrets are required in Actions.

## What stays current

- Featured project cards: public visibility, topics, primary language, stars and latest stable release. Missing/deleted/private repositories disappear from generated cards instead of breaking the whole refresh.
- More public projects: all other owned, non-fork public repositories, alphabetically listed. New repositories appear automatically without guessing a category. The profile repository itself is omitted here.
- Latest posts: newest dated RSS/Atom entries, deduplicated by URL, with the same titles/links in both languages. Titles are not machine-translated.
- Now: the most recently pushed owned, non-fork, non-archived public repositories. Absolute UTC push timestamps remain accurate between scheduled refreshes.
- Public stats: repository counts, stars and forks received for non-fork repositories, followers, and primary-language counts by non-fork repository. These are not private contribution totals, commit totals or language-byte percentages. The two stats card images are an independent display rendered from `stats.base`.
- Recent maintenance: newest merged PRs among the 100 most recently updated closed PRs for the repositories named in `maintenance.repos`. This is intentionally a bounded recent view, not a complete merged-PR history. Fixed old PR/version claims have been removed from project descriptions.

## Site URLs and domain changes

`scripts/profile.config.json` is the only source for the site's own addresses:

- `blog.url` and `blog.feed` fill `AUTO:BLOG_BADGE` (the header badge), `AUTO:BLOG` (the contact line, with the RSS link) and `AUTO:POSTS` (the post links come from the feed itself).
- `stats.base` fills `AUTO:STATS_IMAGES` (the two stats cards).

The hand-written text contains no domain: the introduction, badges and contact copy refer to the blog by name, and every link is generated. To move the site to another domain, edit those three configuration values, run the generator, and commit the two READMEs. No code or prose changes, and no GitHub repository variable is involved.

## What requires the owner

The introduction, interests, location/OS badges, technology-stack icon list, contact/company information, section introductions and collaboration message remain hand-written. They must not be inferred from activity. The profile `bio` is deliberately not read: that text belongs to the profile, not to this repository, and the READMEs own their own wording. The user API request still supplies the follower count used by stats. Featured grouping/order and curated description translations live in `profile.config.json`; descriptions without an override use GitHub's description unchanged, even if it is not in the target language. Keep overrides timeless, or update/remove them when project scope changes. New projects need no configuration to appear in the additional-project list, but deliberate featured placement still needs a config edit.

`exclude_repos` is a case-insensitive denylist applied across cards, activity, catalog and statistics. `lty-moe` is denied so it cannot return even if a repository with that name is recreated. Repository pagination is explicit; private repositories and repositories owned by someone else are rejected even when a personal token is used.

## Run and verify

```sh
python -m unittest discover -s tests -v   # CI runs the same suite as: python -S -m unittest ...
# Optional locally: export GITHUB_TOKEN with public read access for higher API limits.
python scripts/generate_profile.py --snapshot-out /tmp/profile-snapshot.json --report /tmp/profile-report.json
python scripts/generate_profile.py --snapshot-in /tmp/profile-snapshot.json --check
git diff --check
```

A frozen snapshot replay verifies byte-identical generation, bilingual AUTO link parity, expected marker inventory and preservation of all content outside AUTO boundaries. Do not commit snapshots: they are transient public-source evidence. `--check` does not write READMEs and exits nonzero if regeneration would differ; use a frozen snapshot for reproducibility, not a moving live API response.

A generation run may rewrite only `README.md` and `README_zh.md`. The workflow fails if any other tracked file changes, and `git diff --check` rejects whitespace damage. The write path and the `--check` path render from the same snapshot, so a passing replay means the committed files are exactly what the frozen data produces.

## Actions and failure behavior

Actions use the current major versions: `actions/checkout@v7`, `actions/setup-python@v7` and `actions/upload-artifact@v7`. They run on Node 24 and need runner 2.327.1 or newer, which GitHub-hosted `ubuntu-latest` satisfies. Python is pinned to 3.12, the oldest version the generator supports.

The existing daily schedule remains at 03:17 UTC (11:17 China time); GitHub may delay scheduled starts. Changes to scripts, tests, either README or this workflow on main also trigger refresh. Manual dispatch is available. Pull requests run offline tests plus a live-source generation/replay with read-only permissions; they never push. Only successful main-branch runs reach the write-permission update job. A newer pull-request run cancels the superseded one; main runs queue instead of cancelling, so a scheduled refresh and a manual dispatch cannot race to push. Generated updates using `GITHUB_TOKEN` do not recursively trigger the workflow.

GitHub errors (including permission/rate-limit errors) stop generation before writes rather than treating data as deleted. Only latest-release 404 means no release. RSS errors preserve the previous post region in both languages and emit a warning; GitHub-derived regions can still update. All rendering and validation complete before either README is written. The update job stages only the two README files, never force-pushes and fails safely if a human updated main concurrently. Validation uploads the public snapshot, the report, the generated README diff and the interpreter version on every run, including failures; the update job uploads the same evidence when it fails or is cancelled. Artifacts are retained for seven days.

The historical red check on commit `e1193507da89259a9e89ca19ace829a7f8d5f237` was `pre-commit.ci - push`, not the README Actions workflow. Its [result log](https://results.pre-commit.ci/run/github/1000034405/1778823998.PYtoiJ9iRiqQJYU0uWwr_g) says `.pre-commit-config.yaml is not a file`; that commit's Git tree has no file at that path. The new root configuration runs the same offline regression suite in pre-commit.ci. Debricked's separate `neutral` scan-limit output is not a failed Actions run; no App settings were changed.

No automation takes effect on main until the pull request is reviewed and merged. Do not merge or change repository security/App settings merely to make third-party checks green.
