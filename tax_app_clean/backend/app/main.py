from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.tax import router as tax_router

app = FastAPI(title="SecureTax API", version="1.0.0")

# CORS config to allow credentials (HttpOnly cookies) from frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tax_router, prefix="/api/tax", tags=["tax"])

@app.get("/health")
def health_check():
    return {"status": "healthy"}
