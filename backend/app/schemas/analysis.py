from typing import List, Optional
from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, Field

# Shared properties
class AnalysisBase(BaseModel):
    label: Optional[str] = Field(None, description="Custom label for this analysis")

# Properties to receive on creation
class AnalysisCreateRequest(AnalysisBase):
    resume_text: Optional[str] = Field(None, description="The extracted text from the resume. If omitted, uses the saved profile.")
    job_description: str = Field(..., description="The job description to match against")

# Properties to receive on update
class AnalysisUpdateRequest(AnalysisBase):
    pass

# Properties to return to client
class AnalysisResponse(AnalysisBase):
    id: UUID
    user_id: UUID
    match_score: float
    missing_keywords: List[str]
    suggestions: List[str]
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

# Properties for list response (can be expanded with pagination meta later)
class AnalysisListResponse(BaseModel):
    items: List[AnalysisResponse]
    total: int
    page: int
    size: int
