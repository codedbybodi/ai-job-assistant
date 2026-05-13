<<<<<<< HEAD
# AI Job Application Assistant 🤖💼

A production-ready REST API that uses **AI to generate personalized CV summaries, cover letters, and interview tips** for any job application. Built with FastAPI, PostgreSQL, and Google Gemini API.

![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=flat&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-336791?style=flat&logo=postgresql)
![Gemini](https://img.shields.io/badge/Google_Gemini-API-4285F4?style=flat&logo=google)
![JWT](https://img.shields.io/badge/JWT-Auth-black?style=flat&logo=jsonwebtokens)

---

## ✨ Features

- 🔐 **JWT Authentication** — Multi-user support with secure login
- 🤖 **AI-Powered Analysis** — Scrapes company website + analyzes job description
- 📄 **Custom CV Summary** — Tailored to each specific job and company
- ✉️ **Cover Letter Generator** — Professional 3-paragraph cover letter per application
- 🎯 **Interview Tips** — 5 targeted tips based on the job requirements
- 📋 **Application History** — Every user sees only their own saved applications
- 🗄️ **PostgreSQL** — Production-grade relational database with Alembic migrations
- 📖 **Auto-generated docs** — Interactive Swagger UI at `/docs`

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Framework | FastAPI |
| Database | PostgreSQL + SQLAlchemy |
| Migrations | Alembic |
| AI | Google Gemini API (gemini-2.0-flash) |
| Scraping | BeautifulSoup + Requests |
| Auth | JWT (python-jose) + bcrypt |
| Validation | Pydantic v2 |
| Server | Uvicorn |

---

## 📁 Project Structure

```
ai-job-assistant/
├── main.py              # FastAPI app + all routes
├── models.py            # SQLAlchemy DB models (User, Application)
├── schemas.py           # Pydantic request/response schemas
├── database.py          # PostgreSQL connection + session
├── auth.py              # JWT tokens + password hashing
├── services/
│   ├── ai.py            # Google Gemini API integration
│   └── scraper.py       # Company website scraper
├── alembic/             # Database migrations
│   └── versions/
├── alembic.ini          # Alembic config
├── .env                 # Environment variables (not committed)
├── .env.example         # Example env vars for setup
├── requirements.txt     # Python dependencies
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- PostgreSQL 15+
- Google Gemini API key (free at `aistudio.google.com`)

### 1. Clone the repository
```bash
git clone https://github.com/codedbybodi/ai-job-assistant.git
cd ai-job-assistant
```

### 2. Create a virtual environment
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Mac/Linux
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file:
```env
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/jobassistant_db
SECRET_KEY=your-generated-secret-key
GEMINI_API_KEY=your-gemini-api-key
```

Generate a secure secret key:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

### 5. Create the database
```bash
psql -U postgres -c "CREATE DATABASE jobassistant_db;"
```

### 6. Run migrations
```bash
alembic upgrade head
```

### 7. Start the server
```bash
uvicorn main:app --reload
```

- API: `http://localhost:8000`
- Docs: `http://localhost:8000/docs`

---

## 📖 API Endpoints

### Auth

| Method | Endpoint | Description | Auth |
|---|---|---|---|
| POST | `/register` | Create a new account | ❌ |
| POST | `/login` | Login and get JWT token | ❌ |
| GET | `/me` | Get current user info | ✅ |

### Applications

| Method | Endpoint | Description | Auth |
|---|---|---|---|
| POST | `/applications` | Generate AI application materials | ✅ |
| GET | `/applications` | Get all your applications | ✅ |
| GET | `/applications/{id}` | Get single application | ✅ |
| DELETE | `/applications/{id}` | Delete an application | ✅ |

---

## 🧪 Example Usage

### Register
```bash
curl -X POST http://localhost:8000/register \
  -H "Content-Type: application/json" \
  -d '{"name": "AbdulRahman", "email": "test@gmail.com", "password": "123456"}'
```

### Login
```bash
curl -X POST http://localhost:8000/login \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=test@gmail.com&password=123456"
```

### Generate Application Materials
```bash
curl -X POST http://localhost:8000/applications \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "company_url": "https://instabug.com",
    "job_description": "Looking for a Junior Backend Developer with Python and FastAPI experience..."
  }'
```

### Example Response
```json
{
  "id": 1,
  "company_url": "https://instabug.com",
  "cv_summary": "CS student in Cairo with hands-on experience building production APIs...",
  "cover_letter": "Dear Hiring Team at Instabug...",
  "interview_tips": "1. Research Instabug SDK architecture...",
  "created_at": "2026-05-10T13:00:00"
}
```

---

## 🔒 Security

- Passwords hashed with **bcrypt** — never stored in plain text
- JWT tokens expire after **30 minutes**
- Each user can only access **their own** applications
- API keys stored in `.env` — never hardcoded

---

## ⚙️ Migrations

```bash
# After changing models.py
alembic revision --autogenerate -m "describe change"
alembic upgrade head

# Roll back one step
alembic downgrade -1
```

---

## 👨‍💻 Author

**AbdulRahman M.** — CS Student building AI-powered products
=======
# project-structure

-----
```
ai-job-assistant/
├── main.py          ← FastAPI app + routes
├── models.py        ← User + Application DB models
├── schemas.py       ← Pydantic schemas
├── database.py      ← PostgreSQL connection
├── auth.py          ← JWT auth (copy from Week 1)
├── services/
│   ├── scraper.py   ← company website scraper
│   └── ai.py        ← Gemini API analysis
├── alembic/         ← migrations
├── .env
├── requirements.txt
└── README.md
```
>>>>>>> a6975105f771c17ba6569082cb9d4e4dfefd113e
