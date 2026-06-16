import os
from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, status
from pydantic import BaseModel
from app.dependencies import get_current_user
from app.models.user import User
from app.services.file_service import extract_text

router = APIRouter(prefix="/profile", tags=["profile"])

PROFILES_DIR = "data/profiles"

class ProfileResponse(BaseModel):
    has_profile: bool
    resume_text: str | None = None

@router.post("/resume", response_model=ProfileResponse)
async def upload_saved_resume(
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user)
):
    """
    Extracts text from the uploaded resume and saves it as the user's base profile.
    """
    try:
        text = await extract_text(file)
        
        # Save to local file
        file_path = os.path.join(PROFILES_DIR, f"{current_user.id}.txt")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text)
            
        return ProfileResponse(has_profile=True, resume_text=text)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/resume", response_model=ProfileResponse)
async def get_saved_resume(current_user: User = Depends(get_current_user)):
    """
    Returns the user's saved base resume if it exists.
    """
    file_path = os.path.join(PROFILES_DIR, f"{current_user.id}.txt")
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
        return ProfileResponse(has_profile=True, resume_text=text)
    
    return ProfileResponse(has_profile=False, resume_text=None)
