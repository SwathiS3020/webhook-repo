# 📡 Webhook Receiver – Developer Assessment Task (Apr 2021)

This project implements a Flask-based webhook receiver that listens to GitHub events (`push`, `pull_request`, and detected `merge`) from a connected repository (`action-repo`). It stores incoming data in MongoDB and presents it via a live-updating frontend.

---

## 🔧 Tech Stack

- **Backend:** Python (Flask), Flask-CORS
- **Database:** MongoDB
- **Frontend:** HTML, JavaScript
- **Tools:** Ngrok, Postman

---

## 🎯 Project Objectives (per assessment PDF)

- ✅ Receive GitHub Webhooks for Push, PR, and Merge events
- ✅ Store the data using a defined MongoDB schema
- ✅ Display updates in a clean, minimal UI
- ✅ Auto-refresh logs every 15 seconds
- ✅ Bonus: Identify Merge actions from commit messages

---

## 🧾 MongoDB Schema

Each webhook is saved in this structure:

```json
{
  "author": "Swathi",
  "action": "PUSH",
  "from_branch": "dev",
  "to_branch": "main",
  "timestamp": "06 July 2025 - 07:35 PM IST"
}
