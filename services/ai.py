import os 
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def analyze_job(company_info: str, job_description: str, user_name: str) -> dict:
    prompt = f"""
You are an expert career coach helping a junior Python developer apply to jobs

COMPANY_INFO:
{company_info}

JOB DESCRIPTION:
{job_description}

CANDIDATE:
- Name: {user_name}
- CS Student in Cario, Egypt
- Skills: Python, FastAPI, PostgreSQL,  SQLALchemy, JWT Auth, Gemini API, Make.com, Web scraping

Generate exactly these 3 sections with these exact labels:

CV SUMMARY:
(3-4 sentences tailored to this specific job)

COVER LETTER:
(3 professional paragraphs tailored to the company and role)

INTERVIEW TIPS:
(5 specific tips based on this job description)
"""
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )
    text = response.text

    def extract(start, end=None):
        try:
            s = text.index(start) + len(start)
            if end and end in text[s:]:
                return text[s:text.index(end, s)].strip()
        except:
            return text
    return {
        "cv_summary": extract("CV SUMMARY:", "COVER LETTER:"),
        "cover_letter": extract("COVER LETTER:", "INTERVIEW TIPS:"),
        "interview_tips": extract("INTERVIEW TIPS:")
    }