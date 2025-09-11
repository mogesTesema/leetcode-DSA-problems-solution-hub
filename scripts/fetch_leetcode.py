import os, json, requests, pathlib, re

LEETCODE_SESSION = os.environ.get("LEETCODE_SESSION")
LEETCODE_CSRF = os.environ.get("LEETCODE_CSRF_TOKEN")
DEST = pathlib.Path("leetcode")
DEST.mkdir(exist_ok=True)

HEADERS = {
    "Cookie": f"LEETCODE_SESSION={LEETCODE_SESSION}; csrftoken={LEETCODE_CSRF}",
    "x-csrftoken": LEETCODE_CSRF,
    "Referer": "https://leetcode.com",
    "Content-Type": "application/json",
}

GRAPHQL_URL = "https://leetcode.com/graphql"
QUERY = """
query submissions($offset: Int!, $limit: Int!) {
  submissionList(offset: $offset, limit: $limit) {
    submissions {
      id
      title
      titleSlug
      statusDisplay
      lang
      code
      timestamp
    }
    hasNext
  }
}
"""

def fetch_all():
    submissions = []
    offset = 0
    while True:
        resp = requests.post(GRAPHQL_URL, headers=HEADERS, json={"query": QUERY, "variables": {"offset": offset, "limit": 20}})
        data = resp.json()
        if "data" not in data or "submissionList" not in data["data"]:
            print("No submissionList found in response. Possibly auth issue.")
            break
        page = data["data"]["submissionList"]
        subs = page.get("submissions", [])
        if not subs:
            break
        submissions.extend(subs)
        if not page.get("hasNext"):
            break
        offset += 20
    return submissions

def save_submissions(submissions):
    for sub in submissions:
        if sub["statusDisplay"] != "Accepted":
            continue
        slug = re.sub(r"[^a-zA-Z0-9_-]", "_", sub["titleSlug"])
        ext = {"python3": "py", "cpp": "cpp", "java": "java"}.get(sub["lang"], "txt")
        file_path = DEST / f"{slug}.{ext}"
        file_path.write_text(sub["code"])

if __name__ == "__main__":
    subs = fetch_all()
    print(f"Fetched {len(subs)} submissions.")
    save_submissions(subs)
