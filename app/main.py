from fastapi import FastAPI, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session

from dotenv import load_dotenv

from app.database import engine, Base, SessionLocal, get_db
from app import models
from app.models import Experience

from app.routers import (
    certificates,
    personal,
    education,
    skills,
    projects,
    contact,
    experience
)

import os

# Load environment variables
load_dotenv()

# Create database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(
    title="Personal Portfolio API",
    description="API for personal portfolio website",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(
    personal.router,
    prefix="/api",
    tags=["personal"]
)

app.include_router(
    education.router,
    prefix="/api",
    tags=["education"]
)

app.include_router(
    skills.router,
    prefix="/api",
    tags=["skills"]
)

app.include_router(
    projects.router,
    prefix="/api",
    tags=["projects"]
)

app.include_router(
    contact.router,
    prefix="/api",
    tags=["contact"]
)

app.include_router(
    certificates.router,
    prefix="/api",
    tags=["certificates"]
)

app.include_router(
    experience.router,
    prefix="/api",
    tags=["experience"]
)

# Mount static files
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

# Configure templates
templates = Jinja2Templates(directory="templates")


# =========================
# HTML Pages
# =========================

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request}
    )


@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="about.html",
        context={"request": request}
    )


@app.get("/education", response_class=HTMLResponse)
async def education_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="education.html",
        context={"request": request}
    )


@app.get("/skills", response_class=HTMLResponse)
async def skills_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="skills.html",
        context={"request": request}
    )


@app.get("/projects", response_class=HTMLResponse)
async def projects_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="projects.html",
        context={"request": request}
    )


@app.get("/experience", response_class=HTMLResponse)
async def experience_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="experience.html",
        context={"request": request}
    )


@app.get("/contact", response_class=HTMLResponse)
async def contact_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="contact.html",
        context={"request": request}
    )


# =========================
# Health Check
# =========================

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "message": "Portfolio API is running"
    }


# =========================
# Run Server
# =========================

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )