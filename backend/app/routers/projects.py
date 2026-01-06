from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..crud import get_project, get_projects
from ..database import SessionLocal

router = APIRouter(prefix="/projects")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def list_projects(db: Session = Depends(get_db)):
    return get_projects(db)


@router.get("/{slug}")
def project_detail(slug: str, db: Session = Depends(get_db)):
    return get_project(db, slug)
