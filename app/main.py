from fastapi import FastAPI, Request
import hmac
import hashlib
import os

app = FastAPI()

GITHUB_WEBHOOK_SECRET = os.getenv("GITHUB_WEBHOOK_SECRET", "dev-secret")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/webhook/github")
async def github_webhook(request: Request):
    payload = await request.body()
    signature = request.headers.get("X-Hub-Signature-256", "")

    # Verify it's really GitHub sending this
    expected = "sha256=" + hmac.new(
        GITHUB_WEBHOOK_SECRET.encode(), payload, hashlib.sha256
    ).hexdigest()
    if not hmac.compare_digest(expected, signature):
        return {"error": "invalid signature"}, 401

    event = request.headers.get("X-GitHub-Event", "")
    data = await request.json()

    if event == "push":
        repo = data.get("repository", {}).get("full_name")
        commit = data.get("after")
        print(f"[push] repo={repo} commit={commit}")
        # Step for later: trigger Founder 1's deploy API here

    return {"received": True}