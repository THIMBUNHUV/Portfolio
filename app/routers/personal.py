
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter()

@router.get("/hero-info")
async def get_hero_info():
    """Get hero section data for homepage"""
    return {
        "name": "ធីម ប៊ុនហូវ",
        "title": "អ្នកអភិវឌ្ឍកម្មវិធីទូរស័ព្ទដៃ និង វេបសាយ",
        "intro": "ខ្ញុំជានិស្សិតវិស្វកម្មព័ត៌មានវិទ្យា។ មានចំណូលចិត្តក្នុងស្រាវជ្រាវថ្មីៗ និងមានការចាប់អារម្មណ៍ខ្លាំងក្នុងការអភិវឌ្ឍន៍គេហទំព័រ និងកម្មវិធីសម្រាប់ទូរស័ព្ទដៃ។",
        "profile_image": "/static/images/profile.jpg",
        "stats": {
            "projects": 8,
            "experience_years": 2,
            "technologies": 12,
            "certificates": 5
        },
        "buttons": [
            {
                "text": "ទំនាក់ទំនងខ្ញុំ",
                "url": "/contact",
                "icon": "fas fa-envelope",
                "type": "primary"
            },
            {
                "text": "មើលគម្រោង",
                "url": "/projects", 
                "icon": "fas fa-project-diagram",
                "type": "secondary"
            }
        ]
    }

@router.get("/quick-info")
async def get_quick_info():
    """Get quick info cards data"""
    return [
        {
            "icon": "fas fa-map-marker-alt",
            "title": "ទីតាំង",
            "value": "ភ្នំពេញ, កម្ពុជា",
            "color": "#3498db"
        },
        {
            "icon": "fas fa-university", 
            "title": "សាកលវិទ្យាល័យ",
            "value": "សាកលវិទ្យាល័យកម្ពុជា",
            "color": "#9b59b6"
        },
        {
            "icon": "fas fa-calendar-alt",
            "title": "អាយុ",
            "value": "១៩ ឆ្នាំ",
            "color": "#e74c3c"
        },
        {
            "icon": "fas fa-language",
            "title": "ភាសា",
            "value": "ខ្មែរ, អង់គ្លេស",
            "color": "#2ecc71"
        }
    ]