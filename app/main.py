from fastapi import FastAPI
from app.routers import academic, donor, broader_public, decision_makers, general

# Initialize FastAPI app with metadata
app = FastAPI(
    title="LoRAX Summary API",
    description="An API to generate summaries and insights for different audiences using LoRAX.",
    version="1.0.0",
    docs_url="/",  # Swagger UI documentation path
    redoc_url="/redoc",  # ReDoc UI documentation path
    openapi_url="/openapi.json"
)

# Include routers
app.include_router(academic.router, prefix="/api/v1", tags=["Academic"])
app.include_router(donor.router, prefix="/api/v1", tags=["Donor"])
app.include_router(broader_public.router, prefix="/api/v1", tags=["Broader Public"])
app.include_router(decision_makers.router, prefix="/api/v1", tags=["Decision Makers"])
app.include_router(general.router, prefix="/api/v1", tags = ["Manual Prompting"])

# Health check endpoint
@app.get("/health", tags=["Health Check"])
def health_check():
    return {"status": "ok", "message": "API is running!"}
