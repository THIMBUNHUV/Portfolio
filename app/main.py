from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse
from app.routers import certificates, personal, education, skills, projects, contact
import os
from dotenv import load_dotenv
from app.database import engine, Base
from app import models
from fastapi import FastAPI
from app.database import engine, Base
from app import models
from fastapi import Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Experience
from app.database import get_db
from app.routers import experience


Base.metadata.create_all(bind=engine)

load_dotenv()

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



# Include routers
app.include_router(personal.router, prefix="/api", tags=["personal"])
app.include_router(education.router, prefix="/api", tags=["education"])
app.include_router(skills.router, prefix="/api", tags=["skills"])
app.include_router(projects.router, prefix="/api", tags=["projects"])
app.include_router(contact.router, prefix="/api", tags=["contact"])
app.include_router(certificates.router, prefix="/api", tags=["certificates"])


app.include_router(experience.router, prefix="/api", tags=["experience"])

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@app.get("/education", response_class=HTMLResponse)
async def education_page(request: Request):
    return templates.TemplateResponse("education.html", {"request": request})

@app.get("/skills", response_class=HTMLResponse)
async def skills_page(request: Request):
    return templates.TemplateResponse("skills.html", {"request": request})

@app.get("/projects", response_class=HTMLResponse)
async def projects_page(request: Request):
    return templates.TemplateResponse("projects.html", {"request": request})

@app.get("/experience", response_class=HTMLResponse)
async def experience_page(request: Request):
    return templates.TemplateResponse("experience.html", {"request": request})

@app.get("/contact", response_class=HTMLResponse)
async def contact_page(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "Portfolio API is running"}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)