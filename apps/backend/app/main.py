from fastapi import FastAPI

from app.api.v1.health import router as health_router

app = FastAPI(
    title="HONEST DIMENSIONS API",
    description="An AI-powered enterprise knowledge platform.",
    version="0.1.0",
)


app.include_router(
    health_router,
    prefix="/api/v1",
    tags=["Health"]
)


@app.get("/")
async def root():
    return {
        "message": "Welcome to HONEST DIMENSIONS API",
        "version": "0.1.0",
    }