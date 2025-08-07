## 🧠 AI Question Answering with OpenAI Assistant API (Google Cloud Run)

This project is a **serverless Flask-based API** deployed on **Google Cloud Run** that uses the **OpenAI Assistant API** to process and respond to user-submitted questions using a custom GPT-4 assistant.

---

### 🔧 Features

* 🧠 Uses OpenAI **Assistants API** (GPT-4-based)
* 🌐 Accepts a user question via POST and returns a detailed AI-generated answer
* ☁️ Fully deployed on **Google Cloud Run**
* 📦 Minimal dependencies and clean structure
* 🔐 Secure via environment variable for API key

---

### 🧪 Sample Request

```json
POST /
{
  "question": "Give me tips to complete the IELTS reading section in 60 minutes using Test 2"
}
```

### ✅ Sample Response

```json
{
  "answer": "To complete the reading section of the IELTS General Training Test within 60 minutes..."
}
```

---

### 📁 Project Structure

* `main.py` – API logic and assistant call
* `requirements.txt` – Python dependencies
* `Dockerfile` or GCP cloudbuild (optional for deployment)

---

### ⚙️ Tech Stack

* Python 3.12
* Flask (via Functions Framework)
* OpenAI Assistants API (GPT-4)
* Google Cloud Run
* Postman (for testing)
