"""Refresh each chapter's "最後更新 / 最終更新" date from git history.

WHY THIS EXISTS AS A TOOL RATHER THAN A ONE-LINER
-------------------------------------------------
The obvious way to regenerate the field is `git log -1 --format=%ad -- <file>`.
That is WRONG here and fails in a way that looks like success: running this
correction itself creates a commit, so a naive re-run stamps EVERY chapter with
the day the correction ran. The field would then be uniformly wrong instead of
merely stale.

So the definition is:

    最後更新 / 最終更新 = date of the last commit that changed the chapter's
                          CONTENT, excluding commits that only touched the
                          status/date line itself.

This script implements that definition, which means re-running it is safe and
idempotent. It does not depend on anyone having read a warning first.

Usage:
    python tools/refresh_status_dates.py           # report only (default)
    python tools/refresh_status_dates.py --write   # apply changes
"""
import re, subprocess, sys, glob, os

WRITE = "--write" in sys.argv
DATE_KEY = {"cn": "最後更新", "jp": "最終更新"}
# A diff line is "metadata-only" if it is a status line: it carries the date
# key, or the status label itself.
META_PAT = re.compile(r"(最後更新|最終更新|^狀態：|^ステータス：)")


def sh(*args):
    return subprocess.run(args, capture_output=True, text=True,
                          encoding="utf-8", errors="replace").stdout


def commits_for(path):
    out = sh("git", "log", "--format=%H %ad", "--date=short", "--", path)
    return [ln.split(" ", 1) for ln in out.splitlines() if ln.strip()]


def is_metadata_only(sha, path):
    """True if this commit's diff for `path` touches nothing but status lines."""
    diff = sh("git", "show", "--format=", "--unified=0", sha, "--", path)
    touched = [ln[1:] for ln in diff.splitlines()
               if ln[:1] in "+-" and not ln.startswith(("+++", "---"))]
    if not touched:
        return True                      # rename / mode change only
    return all(META_PAT.search(ln.strip()) for ln in touched)


def content_date(path):
    """Date of the newest commit that changed real content."""
    for sha, date in commits_for(path):
        if not is_metadata_only(sha, path):
            return date
    return None                          # only ever had metadata commits


def preflight():
    """Refuse to run where the derivation would be silently wrong.

    The exclusion logic walks commit history. On a shallow clone the commits
    below the boundary simply do not exist as far as git is concerned, so a
    chapter's date resolves to the earliest VISIBLE commit -- and the script
    would still exit 0 with a perfectly plausible-looking date. That is the
    same "fails in a way that looks like success" mode this tool exists to
    prevent, so it is an error rather than a warning.
    """
    if sh("git", "rev-parse", "--is-inside-work-tree").strip() != "true":
        sys.exit("ERROR: not inside a git work tree; content dates cannot be derived.")
    if sh("git", "rev-parse", "--is-shallow-repository").strip() == "true":
        sys.exit("ERROR: shallow clone detected.\n"
                 "  Commits below the shallow boundary are invisible, so every date\n"
                 "  would silently resolve to the earliest visible commit.\n"
                 "  Run `git fetch --unshallow` first, then re-run this script.")


def main():
    preflight()
    changed = errors = 0
    files = sorted(glob.glob("cn/*.md")) + sorted(glob.glob("jp/*.md"))
    for raw in files:
        path = raw.replace(os.sep, "/")          # Windows glob yields backslashes
        lang = path.split("/")[0]
        key = DATE_KEY.get(lang)
        if not key:
            continue
        text = open(path, "rb").read().decode("utf-8")
        crlf = "\r\n" in text
        flat = text.replace("\r\n", "\n")
        m = re.search(key + r" (\d{4}-\d{2}-\d{2})", flat)
        if not m:
            continue                             # no status line (e.g. TERMS.md)
        stated = m.group(1)
        actual = content_date(path)
        if actual is None:
            print(f"  ?? {path}: no content commit found"); errors += 1; continue
        if stated == actual:
            continue
        print(f"  {path}: {stated} -> {actual}")
        changed += 1
        if WRITE:
            new = flat.replace(f"{key} {stated}", f"{key} {actual}", 1)
            out = new.replace("\n", "\r\n") if crlf else new
            open(path, "wb").write(out.encode("utf-8"))

    if changed == 0:
        print("All chapter dates already match their last content change.")
    elif not WRITE:
        print(f"\n{changed} file(s) would change. Re-run with --write to apply.")
    else:
        print(f"\n{changed} file(s) updated.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
