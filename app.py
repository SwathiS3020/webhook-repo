from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)
CORS(app)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["webhook_db"]
collection = db["webhook_logs"]

# Homepage UI
@app.route('/')
def index():
    return render_template("index.html")

# Webhook endpoint
@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        payload = request.json
        event_type = request.headers.get("X-GitHub-Event", "").upper()
        sender = payload.get("sender", {}).get("login", "unknown")

        from_branch = ""
        to_branch = ""

        if event_type == "PULL_REQUEST":
            pr = payload.get("pull_request", {})
            from_branch = pr.get("head", {}).get("ref", "")
            to_branch = pr.get("base", {}).get("ref", "")
        elif event_type == "PUSH":
            from_branch = payload.get("ref", "").split("/")[-1]
            to_branch = payload.get("repository", {}).get("default_branch", "")
            if "merge" in payload.get("head_commit", {}).get("message", "").lower():
                event_type = "MERGE"
        else:
            # fallback branch detection
            from_branch = payload.get("ref", "").split("/")[-1]
            to_branch = payload.get("repository", {}).get("default_branch", "")

        log = {
            "author": sender,
            "action": event_type,
            "from_branch": from_branch,
            "to_branch": to_branch,
            "timestamp": datetime.utcnow().strftime("%d %B %Y - %I:%M %p UTC")
        }

        collection.insert_one(log)
        return jsonify({"status": "stored", "data": log}), 200

    except Exception as e:
        print("❌ Error:", str(e))
        return jsonify({"error": str(e)}), 500

@app.route('/logs', methods=['GET'])
def get_logs():
    logs = list(collection.find().sort('_id', -1).limit(10))
    for log in logs:
        log['_id'] = str(log['_id'])  # convert ObjectId to string
    return jsonify(logs), 200
if __name__ == '__main__':
    app.run(debug=True, port=5000)
