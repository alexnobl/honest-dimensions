from typing import Literal

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from app.database.session import engine

router = APIRouter()


class HealthResponse(BaseModel):
    status: Literal["healthy"]
    service: str
    version: str


@router.get("/health", response_model=HealthResponse)
async def health_check():
    return HealthResponse(
        status="healthy",
        service="honest-dimensions-backend",
        version="0.1.0",
    )


@router.get("/health/ready")
def readiness_check():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

            vector_version = connection.execute(
                text(
                    "SELECT extversion FROM pg_extension "
                    "WHERE extname = 'vector'"
                )
            ).scalar_one_or_none()

    except SQLAlchemyError:
        raise HTTPException(
            status_code=503,
            detail={
                "status": "unavailable",
                "database": "unavailable",
            },
        )

    if vector_version is None:
        raise HTTPException(
            status_code=503,
            detail={
                "status": "unavailable",
                "database": "connected",
                "vector_extension": "missing",
            },
        )

    return {
        "status": "ready",
        "database": "connected",
        "vector_extension": vector_version,
    }