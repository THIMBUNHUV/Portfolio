from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas
from app.database import get_db

router = APIRouter()

@router.get("/projects", response_model=List[schemas.Project])
def read_projects(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    projects = crud.get_projects(db, skip=skip, limit=limit)
    return projects

@router.post("/projects", response_model=schemas.Project)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    return crud.create_project(db=db, project=project)

@router.get("/projects/sample")
def get_sample_projects():
    return [
        {
            "id": 1,
            "title": "វេបសាយប្រវត្តិរូប",
            "description": "វេបសាយបង្ហាញពីជំនាញ ការអប់រំ និងគម្រោងផ្ទាល់ខ្លួន។ បង្កើតឡើងដោយប្រើ FastAPI និង PostgreSQL។",
            "technologies": "FastAPI, PostgreSQL, HTML, CSS, JavaScript",
            "github_link": "https://github.com/soksamnang/portfolio",
            "demo_link": "https://portfolio-soksamnang.render.com",
            "image_url": "/static/images/project1.jpg",
            "created_at": "2025-12-15T00:00:00"
        },
        {
            "id": 2,
            "title": "ប្រព័ន្ធគ្រប់គ្រងសាលា",
            "description": "ប្រព័ន្ធសម្រាប់គ្រប់គ្រងសិស្ស បុគ្គលិក និងថ្នាក់រៀននៅក្នុងសាលា។",
            "technologies": "Python, Django, PostgreSQL, Bootstrap",
            "github_link": "https://github.com/soksamnang/school-management",
            "demo_link": "https://school-management-demo.render.com",
            "image_url": "/static/images/project2.jpg",
            "created_at": "2025-10-20T00:00:00"
        },
        {
            "id": 3,
            "title": "កម្មវិធីទូរស័ព្ទទំនាក់ទំនង",
            "description": "កម្មវិធីសម្រាប់ទូរស័ព្ទដៃសម្រាប់ទំនាក់ទំនងជាមួយមិត្តភក្តិ និងក្រុមគ្រួសារ។",
            "technologies": "React Native, Firebase, Node.js",
            "github_link": "https://github.com/soksamnang/chat-app",
            "demo_link": "https://chat-app-demo.com",
            "image_url": "/static/images/project3.jpg",
            "created_at": "2025-08-10T00:00:00"
        }
    ]