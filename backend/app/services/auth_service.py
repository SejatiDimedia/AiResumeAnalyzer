from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException, status
import uuid
from datetime import datetime, timedelta

from app.models.user import User, PasswordResetToken
from app.schemas.auth import RegisterRequest
from app.utils.security import get_password_hash, verify_password
from app.config import settings

async def create_user(db: AsyncSession, request: RegisterRequest) -> User:
    # Check if user already exists
    result = await db.execute(select(User).where(User.email == request.email))
    existing_user = result.scalars().first()
    
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    new_user = User(
        email=request.email,
        hashed_password=get_password_hash(request.password)
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

async def authenticate_user(db: AsyncSession, email: str, password: str) -> User:
    result = await db.execute(select(User).where(User.email == email))
    user = result.scalars().first()
    
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user

async def get_user_by_id(db: AsyncSession, user_id: uuid.UUID) -> User:
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalars().first()

async def create_reset_token(db: AsyncSession, email: str) -> PasswordResetToken:
    result = await db.execute(select(User).where(User.email == email))
    user = result.scalars().first()
    
    if not user:
        # Prevent email enumeration by returning successfully anyway or raising generic
        raise HTTPException(status_code=404, detail="User not found")
        
    token = str(uuid.uuid4())
    expires_at = datetime.utcnow() + timedelta(hours=1)
    
    reset_token = PasswordResetToken(
        email=email,
        token=token,
        expires_at=expires_at
    )
    db.add(reset_token)
    await db.commit()
    await db.refresh(reset_token)
    return reset_token

async def reset_password(db: AsyncSession, token: str, new_password: str) -> bool:
    result = await db.execute(select(PasswordResetToken).where(PasswordResetToken.token == token))
    reset_token = result.scalars().first()
    
    if not reset_token:
        raise HTTPException(status_code=400, detail="Invalid token")
    if reset_token.used:
        raise HTTPException(status_code=400, detail="Token already used")
    if reset_token.expires_at < datetime.utcnow():
        raise HTTPException(status_code=400, detail="Token expired")
        
    # Update password
    result = await db.execute(select(User).where(User.email == reset_token.email))
    user = result.scalars().first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
        
    user.hashed_password = get_password_hash(new_password)
    reset_token.used = True
    
    await db.commit()
    return True
