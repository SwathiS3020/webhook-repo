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
---

## 🌐 Ngrok Public URL – Please Read Before Testing

> **Note for the Reviewer:**  
> This project uses [ngrok](https://ngrok.com/) to expose the Flask application running on `localhost:5000` to the public internet so GitHub can send webhook events to it.

### ❓ Why ngrok?

GitHub webhooks require a **publicly accessible URL** to deliver payloads. Since this application runs locally during development, we use `ngrok` to generate a temporary public URL that tunnels to `localhost`.

---

### ⚠️ Important Limitation of ngrok Free Plan

When using the free version of ngrok:

- The public URL changes **every time ngrok is restarted**
- The webhook URL configured in GitHub must be updated **each time** the ngrok URL changes
- If the old URL is used or ngrok is not running, you will get a `404 Not Found` or `ERR_NGROK_3200`

---

### 🛠️ How to Test This Project 

If you wish to test this project on your machine:

1. Install [ngrok](https://ngrok.com/download)
2. Start your local Flask server:

   ```bash
   python app.py


### 🖼️ Webhook Frontend UI

![Webhook Frontend UI](screenshots/ui-screenshot.png)



