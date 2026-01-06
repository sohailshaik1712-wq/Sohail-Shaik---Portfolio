from app.database import SessionLocal
from app.models import Project
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter(prefix="/admin")

ADMIN_KEY = "sohail-admin"


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def authorize(key: str):
    if key != ADMIN_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")


@router.post("/projects")
def create_project(project: dict, key: str, db: Session = Depends(get_db)):
    authorize(key)
    p = Project(**project)
    db.add(p)
    db.commit()
    return {"status": "created"}


@router.put("/projects/{slug}")
def update_project(slug: str, project: dict, key: str, db: Session = Depends(get_db)):
    authorize(key)
    p = db.query(Project).filter(Project.slug == slug).first()
    for k, v in project.items():
        setattr(p, k, v)
    db.commit()
    return {"status": "updated"}


@router.delete("/projects/{slug}")
def delete_project(slug: str, key: str, db: Session = Depends(get_db)):
    authorize(key)
    p = db.query(Project).filter(Project.slug == slug).first()
    db.delete(p)
    db.commit()
    return {"status": "deleted"}
