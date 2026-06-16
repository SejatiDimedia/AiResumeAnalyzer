from pydantic import BaseModel, Field
from typing import List
from google import genai
from app.config import settings
import logging

logger = logging.getLogger(__name__)

# Initialize the Gemini client
client = genai.Client(api_key=settings.GEMINI_API_KEY)

class AIAnalysisResult(BaseModel):
    match_score: float = Field(description="A score out of 100 representing how well the resume matches the job description.")
    missing_keywords: List[str] = Field(description="A list of important skills or keywords present in the job description but missing from the resume.")
    suggestions: List[str] = Field(description="Actionable suggestions on how the candidate can improve their resume for this specific role.")

async def analyze_resume_vs_jd(resume_text: str, job_description: str) -> AIAnalysisResult:
    """
    Calls Google Gemini to analyze the given resume text against the job description.
    Uses Structured Outputs to ensure the response strictly follows the AIAnalysisResult schema.
    """
    if not settings.GEMINI_API_KEY:
        logger.warning("GEMINI_API_KEY is not set! Returning mock data instead of calling Gemini.")
        return AIAnalysisResult(
            match_score=0.0,
            missing_keywords=["API Key Missing"],
            suggestions=["Please configure the GEMINI_API_KEY in the backend .env file."]
        )

    # Phase 4: Input Sanitization / Security
    # Truncate inputs to prevent excessive token usage
    max_resume_words = 8000
    max_jd_words = 3000
    
    resume_words = resume_text.split()
    if len(resume_words) > max_resume_words:
        logger.warning(f"Resume text exceeded {max_resume_words} words. Truncating.")
        resume_text = " ".join(resume_words[:max_resume_words])
        
    jd_words = job_description.split()
    if len(jd_words) > max_jd_words:
        logger.warning(f"Job description exceeded {max_jd_words} words. Truncating.")
        job_description = " ".join(jd_words[:max_jd_words])

    system_prompt = (
        "You are an expert technical recruiter and resume analyzer. "
        "Your task is to analyze a candidate's resume against a provided job description. "
        "Calculate a fair match score (0-100), identify key skills or keywords missing from the resume, "
        "and provide actionable suggestions for improvement."
    )

    user_prompt = f"""
### Job Description:
{job_description}

### Candidate Resume:
{resume_text}
"""

    try:
        response = await client.aio.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_prompt,
            config=genai.types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=AIAnalysisResult,
                system_instruction=system_prompt,
                temperature=0.2
            )
        )
        
        result = response.parsed
        return result
    except Exception as e:
        logger.error(f"Error calling Gemini API: {str(e)}")
        # In case of network errors or other exceptions, raise or return a fallback
        raise e

async def generate_cover_letter(resume_text: str, job_description: str, job_title: str = "") -> str:
    """
    Calls Google Gemini to generate a tailored cover letter based on
    the candidate's resume and the job description.
    Returns a plain string containing the cover letter.
    """
    if not settings.GEMINI_API_KEY:
        return "API Key Missing. Please configure the GEMINI_API_KEY in the backend .env file."

    system_prompt = (
        "You are an expert career coach and professional writer specializing in job applications. "
        "Your task is to write a compelling, tailored cover letter for a job applicant. "
        "The letter should be professional, concise (3-4 paragraphs), and highlight the candidate's "
        "relevant strengths that match the job description. "
        "Do NOT include placeholder text like [Your Name] or [Date]. "
        "Write the body of the letter only — start directly with 'Dear Hiring Manager,' "
        "and end with a professional closing like 'Sincerely,' followed by a blank signature line."
    )

    title_context = f" for the position of {job_title}" if job_title else ""
    user_prompt = f"""
    Please write a tailored cover letter{title_context}.

    ### Job Description:
    {job_description}

    ### Candidate Resume:
    {resume_text}
    """

    try:
        response = await client.aio.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_prompt,
            config=genai.types.GenerateContentConfig(
                system_instruction=system_prompt,
                temperature=0.7
            )
        )
        return response.text
    except Exception as e:
        logger.error(f"Error calling Gemini API for cover letter: {str(e)}")
        raise e
