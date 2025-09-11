import os
import json
import requests
import pathlib
import re

# ------------------ CONFIG ------------------
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

# GraphQL query to fetch submissions
GRAPHQL_URL = "https://leetcode.com/graphql"
SUBMISSIONS_QUERY = """
query submissionList($offset: Int!, $limit: Int!) {
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

# GraphQL query to get problem difficulty
QUESTION_QUERY = """
query getQuestionDetail($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    difficulty
  }
}
"""

def fetch_all_submissions():
    submissions = []
    offset = 0
    while True:
        resp = requests.post(
            GRAPHQL_URL,
            headers=HEADERS,
            json={"query": SUBMISSIONS_QUERY, "variables": {"offset": offset, "limit": 20}}
        )
        data = resp.json()
        sublist = data.get("data", {}).get("submissionList", {}).get("submissions")
        if not sublist:
            break
        submissions.extend(sublist)
        if not data["data"]["submissionList"].get("hasNext", False):
            break
        offset += 20
    return submissions

def get_difficulty(titleSlug):
    resp = requests.post(
        GRAPHQL_URL,
        headers=HEADERS,
        json={"query": QUESTION_QUERY, "variables": {"titleSlug": titleSlug}}
    )
    data = resp.json()
    return data.get("data", {}).get("question", {}).get("difficulty", "Unknown")

def save_submission(sub):
    if sub["statusDisplay"] != "Accepted":
        return
    slug = re.sub(r"[^a-zA-Z0-9_-]", "_", sub["titleSlug"])
    ext = {"python3": "py", "cpp": "cpp", "java": "java"}.get(sub["lang"], "txt")
    file_path = DEST / f"{slug}.{ext}"
    file_path.write_text(sub["code"])

    # Save metadata for counting
    metadata = {
        "title": sub["title"],
        "slug": slug,
        "lang": sub["lang"],
        "difficulty": get_difficulty(sub["titleSlug"]),
        "timestamp": sub["timestamp"]
    }
    meta_path = DEST / f"{slug}.json"
    meta_path.write_text(json.dumps(metadata, indent=2))

if __name__ == "__main__":
    submissions = fetch_all_submissions()
    if not submissions:
        print("No submissions fetched. Exiting.")
        exit(0)

    for sub in submissions:
        save_submission(sub)

    print(f"Fetched and saved {len(submissions)} submissions.")
