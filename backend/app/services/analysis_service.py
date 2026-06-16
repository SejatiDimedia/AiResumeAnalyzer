from uuid import UUID
from typing import Tuple, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import func
from app.models.analysis import Analysis
from app.schemas.analysis import AnalysisCreateRequest, AnalysisUpdateRequest

async def create_analysis(db: AsyncSession, user_id: UUID, obj_in: AnalysisCreateRequest) -> Analysis:
    # TODO in Phase 2: Integrate with OpenAI here.
    # For Phase 1.3, we will mock the AI result
    mock_score = 85.5
    mock_missing = ["Docker", "Kubernetes"]
    mock_suggestions = ["Add more details about your Docker experience", "Mention Kubernetes orchestration"]
    
    db_obj = Analysis(
        user_id=user_id,
        resume_text=obj_in.resume_text,
        job_description=obj_in.job_description,
        label=obj_in.label,
        match_score=mock_score,
        missing_keywords=mock_missing,
        suggestions=mock_suggestions
    )
    db.add(db_obj)
    await db.commit()
    await db.refresh(db_obj)
    return db_obj

async def get_analysis_by_id(db: AsyncSession, analysis_id: UUID, user_id: UUID) -> Analysis | None:
    stmt = select(Analysis).where(
        Analysis.id == analysis_id,
        Analysis.user_id == user_id,
        Analysis.is_deleted == False
    )
    result = await db.execute(stmt)
    return result.scalar_one_or_none()

async def list_user_analyses(db: AsyncSession, user_id: UUID, page: int = 1, size: int = 10) -> Tuple[List[Analysis], int]:
    offset = (page - 1) * size
    
    # Query for items
    stmt = select(Analysis).where(
        Analysis.user_id == user_id,
        Analysis.is_deleted == False
    ).order_by(Analysis.created_at.desc()).offset(offset).limit(size)
    result = await db.execute(stmt)
    items = result.scalars().all()
    
    # Query for total count
    count_stmt = select(func.count()).select_from(Analysis).where(
        Analysis.user_id == user_id,
        Analysis.is_deleted == False
    )
    count_result = await db.execute(count_stmt)
    total = count_result.scalar_one()
    
    return items, total

async def update_analysis_label(db: AsyncSession, analysis_id: UUID, user_id: UUID, obj_in: AnalysisUpdateRequest) -> Analysis | None:
    db_obj = await get_analysis_by_id(db, analysis_id, user_id)
    if not db_obj:
        return None
        
    db_obj.label = obj_in.label
    await db.commit()
    await db.refresh(db_obj)
    return db_obj

async def soft_delete_analysis(db: AsyncSession, analysis_id: UUID, user_id: UUID) -> bool:
    db_obj = await get_analysis_by_id(db, analysis_id, user_id)
    if not db_obj:
        return False
        
    db_obj.is_deleted = True
    await db.commit()
    return True
