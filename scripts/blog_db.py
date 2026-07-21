#!/usr/bin/env python3
import html
import json
import re
import sys
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = REPO_ROOT / "blog" / "articles.json"
HTML_PATH = REPO_ROOT / "blog.html"
LIST_START = "<!-- ARTICLE_LIST:START -->"
LIST_END = "<!-- ARTICLE_LIST:END -->"


def load_db():
    if DB_PATH.exists():
        return json.loads(DB_PATH.read_text())
    return []


def save_db(entries):
    DB_PATH.write_text(json.dumps(entries, indent=2) + "\n")


def normalize_path(path_str):
    p = Path(path_str)
    p = p if p.is_absolute() else (Path.cwd() / p)
    p = p.resolve()
    try:
        rel = p.relative_to(REPO_ROOT)
    except ValueError:
        raise SystemExit(f"Path must be inside the repo: {path_str}")
    if rel.parts[0] != "blog":
        raise SystemExit(f"Articles must live under blog/: {rel}")
    return rel


def post_id_for(rel_path):
    return str(rel_path.relative_to("blog").with_suffix(""))


def render_html(entries):
    ordered = sorted(entries, key=lambda e: e["date_created"], reverse=True)
    items = "\n".join(
        f'                <li><a href="blog.html?post={e["post"]}">{html.escape(e["name"])}</a></li>'
        for e in ordered
    )
    new_block = f'<ul class="blog-list">\n{items}\n            </ul>'

    contents = HTML_PATH.read_text()
    pattern = re.compile(re.escape(LIST_START) + r".*?" + re.escape(LIST_END), re.DOTALL)
    if not pattern.search(contents):
        raise SystemExit(f"Could not find {LIST_START} / {LIST_END} markers in {HTML_PATH}")
    contents = pattern.sub(f"{LIST_START}\n            {new_block}\n            {LIST_END}", contents)
    HTML_PATH.write_text(contents)


def cmd_add(path_str, name):
    rel = normalize_path(path_str)
    if not (REPO_ROOT / rel).exists():
        raise SystemExit(f"No such file: {rel}")
    entries = load_db()
    if any(Path(e["path"]) == rel for e in entries):
        raise SystemExit(f"Article already indexed: {rel} (use update-name to rename it)")
    today = date.today().isoformat()
    entries.append({
        "path": str(rel),
        "post": post_id_for(rel),
        "name": name,
        "date_created": today,
        "date_updated": today,
    })
    save_db(entries)
    render_html(entries)
    print(f"Added '{name}' ({rel})")


def cmd_remove(path_str):
    rel = normalize_path(path_str)
    entries = load_db()
    match = next((e for e in entries if Path(e["path"]) == rel), None)
    if match is None:
        raise SystemExit(f"No indexed article with path: {rel}")
    entries = [e for e in entries if Path(e["path"]) != rel]
    save_db(entries)
    render_html(entries)
    print(f"Removed '{match['name']}' ({rel}) from the index. The file itself was left on disk.")


def cmd_update_name(path_str, new_name):
    rel = normalize_path(path_str)
    entries = load_db()
    match = next((e for e in entries if Path(e["path"]) == rel), None)
    if match is None:
        raise SystemExit(f"No indexed article with path: {rel}")
    old_name = match["name"]
    match["name"] = new_name
    match["date_updated"] = date.today().isoformat()
    save_db(entries)
    render_html(entries)
    print(f"Renamed '{old_name}' -> '{new_name}' ({rel})")


def cmd_list():
    entries = load_db()
    if not entries:
        print("No articles indexed.")
        return
    ordered = sorted(entries, key=lambda e: e["date_created"], reverse=True)
    name_width = max(len(e["name"]) for e in ordered)
    path_width = max(len(e["path"]) for e in ordered)
    for e in ordered:
        print(
            f'{e["name"]:<{name_width}}  {e["path"]:<{path_width}}  '
            f'created {e["date_created"]}  updated {e["date_updated"]}'
        )


def main():
    if len(sys.argv) < 2:
        raise SystemExit("usage: blog_db.py <add|remove|update-name|list> ...")
    cmd, args = sys.argv[1], sys.argv[2:]
    if cmd == "add" and len(args) == 2:
        cmd_add(*args)
    elif cmd == "remove" and len(args) == 1:
        cmd_remove(*args)
    elif cmd == "update-name" and len(args) == 2:
        cmd_update_name(*args)
    elif cmd == "list" and len(args) == 0:
        cmd_list()
    else:
        raise SystemExit(f"bad invocation: {cmd} {args}")


if __name__ == "__main__":
    main()
