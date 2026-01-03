import os
import json
import urllib.request
import datetime

# ===================== CONFIG =====================
REPO_OWNER = "hihi333444jj"
REPO_NAME = "PygemaRenderSof"
BRANCH = "main"  # change to "master" if needed
API_BASE = "https://api.github.com"
RAW_BASE = f"https://raw.githubusercontent.com/{REPO_OWNER}/{REPO_NAME}/{BRANCH}"
# ==================================================


def github_api(url):
    req = urllib.request.Request(
        url,
        headers={"Accept": "application/vnd.github.v3+json"}
    )
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read().decode())


def get_repo_tree():
    url = f"{API_BASE}/repos/{REPO_OWNER}/{REPO_NAME}/git/trees/{BRANCH}?recursive=1"
    return github_api(url)["tree"]


def get_last_commit_time(path):
    url = f"{API_BASE}/repos/{REPO_OWNER}/{REPO_NAME}/commits?path={path}&per_page=1"
    data = github_api(url)
    if not data:
        return None
    commit_time = data[0]["commit"]["committer"]["date"]
    return datetime.datetime.fromisoformat(
        commit_time.replace("Z", "+00:00")
    ).timestamp()


def download_file(path):
    url = f"{RAW_BASE}/{path}"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    urllib.request.urlretrieve(url, path)


def ask_user(path, reason):
    while True:
        choice = input(f"{reason}: {path}\nUpdate this file? (y/n): ").strip().lower()
        if choice in ("y", "n"):
            return choice == "y"


def sync():
    print("Scanning GitHub repository...\n")
    tree = get_repo_tree()

    for item in tree:
        if item["type"] != "blob":
            continue

        path = item["path"]
        github_time = get_last_commit_time(path)
        if github_time is None:
            continue

        if os.path.exists(path):
            local_time = os.path.getmtime(path)
            if github_time > local_time:
                if ask_user(path, "Outdated file"):
                    print("  → Updating")
                    download_file(path)
                    os.utime(path, (github_time, github_time))
                else:
                    print("  → Skipped")
        else:
            if ask_user(path, "Missing file"):
                print("  → Downloading")
                download_file(path)
                os.utime(path, (github_time, github_time))
            else:
                print("  → Skipped")

    print("\nSync complete.")


if __name__ == "__main__":
    sync()
