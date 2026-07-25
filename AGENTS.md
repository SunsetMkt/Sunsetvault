# AGENTS.md

## Project identity

This is **not a source-code repo**. It is a CI/CD patching pipeline that clones `bitwarden/clients`, rebrands it as Sunsetvault, builds browser extensions, and publishes releases. There is no local build — everything runs in GitHub Actions on `ubuntu-22.04`.

Upstream source: `https://github.com/bitwarden/clients` — cloned fresh by every CI run.

## Workflow chain

3 numbered workflows triggered in sequence via `gh workflow run`:

```
1. Check Browser (check-browser.yml)  →  2. Build Browser (build-browser.yml)  →  3. Release Browser (release-browser.yml)
```

- **`1. Check Browser`**: Daily cron (`0 0 * * *`) + manual. Uses `git ls-remote` to find latest upstream `browser` tag, compares against `latest_browser_tag.txt`. If new → commits tag file → `gh workflow run build-browser.yml`.
- **`2. Build Browser`**: Receives `tag` via `workflow_dispatch`. Clones upstream, applies patches, builds Chrome/Edge/Firefox/Opera via npm.
- **`3. Release Browser`**: Receives `tag` + `run_id`. Downloads artifacts from the build run, normalizes zips with `strip-nondeterminism`, computes SHA256, creates GitHub Release.

All `gh workflow run` calls require a prior `actions/checkout` step — `gh` needs a local `.git` directory.

## Branch and file conventions

- Default branch is **`main`** (not `master`).
- Every workflow step that accepts/produces parameters must print them (`echo "tag=${{ inputs.tag }}"`, etc.).
- `latest_browser_tag.txt` is an empty tracked file that the check workflow updates on new upstream tags. It starts empty — the first run populates it.

## Patching system

Patches are applied in `build-source` job of `2. Build Browser`:

| File                              | Target                                      | Effect                                                                   |
| --------------------------------- | ------------------------------------------- | ------------------------------------------------------------------------ |
| `patches/patchManifestV2.py`      | `clients/apps/browser/src/manifest.json`    | Rebrands name, author, icons, extension ID                               |
| `patches/patchManifestV3.py`      | `clients/apps/browser/src/manifest.v3.json` | Same for Manifest V3                                                     |
| `patches/fakePremium.patch`       | `libs/common/src/billing/…` (git apply)     | Forces `hasPremiumPersonally=true`, `hasPremiumFromAnyOrganization=true` |
| `patches/images/icon*_sunset.png` | copied to `apps/browser/src/images/`        | 7 sizes (16–512px) of sunset icon                                        |

The Python manifest scripts run **before** `cd clients` — they operate on `clients/apps/browser/src/manifest*.json` from the workspace root.

Generate icons: `pip install pillow && python generate_icons.py` → writes 7 PNGs to `patches/images/`. Not required for CI.

## Key gotchas

- **`setup-node` with npm cache**: The `build` matrix job in `2. Build Browser` must download and unzip `browser-source` **before** `actions/setup-node`, otherwise `cache-dependency-path: "**/package-lock.json"` fails with "Some specified paths were not resolved".
- **`git ls-remote` pipes**: Avoid `git ls-remote | awk` in a pipeline — GitHub Actions `pipefail` causes exit 141 (SIGPIPE) when `awk` exits early. Use a temp file: `git ls-remote … > /tmp/tags.txt; awk … /tmp/tags.txt`.
- **`gh workflow run` needs `.git`**: Always run it after `actions/checkout`, or use `--repo ${{ github.repository }}`.
- **`download-artifact` by `run-id`**: Downloads all artifacts from a prior run. Extracts each artifact into a subdirectory named after the artifact. Files appear at `artifacts/*/*.zip`.
- **Firefox MV3 is intentionally disabled**: Commented out in the matrix with artifact name "DO-NOT-USE-FOR-PROD". Do not enable.
- **Reproducible builds**: `strip-nondeterminism` (apt package) normalizes zip timestamps, permissions, and ordering. Pinned to `ubuntu-22.04` for consistent toolchain.
- **Artifact names include tag**: `dist-chrome-MV3-$TAG.zip`, `dist-firefox-$TAG.zip`, etc. The `browser-source` artifact also uses this pattern.
- **locales-test `# exit 1`** and **Firefox size check `# exit 1`** are intentionally commented out — failures are warnings only.
- **Self-push**: The check workflow commits to `main` via `github-actions[bot]`. Ensure branch protection rules allow this.
