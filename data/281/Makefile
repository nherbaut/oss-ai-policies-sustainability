CSV ?= dataset1-multiple-ai-policies.csv
OUT ?= policies

define DOWNLOAD
import csv
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlsplit
from urllib.request import Request, urlopen

fields = ((9, "ai_policy"), (10, "contributing"), (11, "agent"), (13, "other_policy"))
errors = 0

def raw_url(url):
    parsed = urlsplit(url)
    parts = parsed.path.strip("/").split("/", 4)
    if parsed.netloc.lower() == "github.com" and len(parts) == 5 and parts[2] == "blob":
        return "https://raw.githubusercontent.com/" + "/".join((parts[0], parts[1], parts[3], parts[4]))
    return url

with open(sys.argv[1], newline="", encoding="utf-8-sig") as source:
    rows = csv.reader(source)
    next(rows, None)  # Skip header
    for row in rows:
        if not row or not row[0].strip():
            continue
        repo = row[0].strip()
        parts = repo.split("/")
        if any(part in ("", ".", "..") for part in parts):
            print(f"Invalid repository path: {repo}", file=sys.stderr)
            errors += 1
            continue
        folder = Path(sys.argv[2]).joinpath(*parts)
        folder.mkdir(parents=True, exist_ok=True)
        for index, name in fields:
            if len(row) <= index or not row[index].strip():
                continue
            url = row[index].strip()
            try:
                nlnet_url = "https://nlnet.nl/foundation/policies/generativeAI/2.0/"
                shared_policy = Path(sys.argv[2]) / "diesel-rs/diesel/other_policy.md"
                is_nlnet_policy = url.rstrip("/") in (nlnet_url.rstrip("/"), nlnet_url.rsplit("/2.0/", 1)[0])
                if is_nlnet_policy:
                    url = nlnet_url
                    if shared_policy.is_file() and shared_policy.read_bytes().strip():
                        print(f"{repo}: shared foundation policy: {shared_policy}")
                        continue
                request = Request(raw_url(url), headers={"User-Agent": "Mozilla/5.0"})
                with urlopen(request, timeout=30) as response:
                    data = response.read()
                    media_type = response.headers.get_content_type()
                ext = Path(urlsplit(url).path).suffix.lower()
                if ext in (".html", ".htm") or media_type == "text/html":
                    data = subprocess.run(
                        ["pandoc", "-f", "html", "-t", "gfm"],
                        input=data, capture_output=True, check=True
                    ).stdout
                elif ext not in ("", ".md", ".markdown") and media_type != "text/markdown":
                    raise ValueError("Unsupported file type (expected Markdown or HTML)")
                dest = shared_policy if is_nlnet_policy else folder / f"{name}.md"
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(data)
                print(f"{repo}: {dest}")
            except (OSError, ValueError, subprocess.CalledProcessError) as e:
                print(f"{repo}: {url}: {e}", file=sys.stderr)
                errors += 1
if errors:
    sys.exit(1)
endef
export DOWNLOAD

.PHONY: all
all:
	@python3 -c "$$DOWNLOAD" "$(CSV)" "$(OUT)"
