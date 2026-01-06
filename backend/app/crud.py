from sqlalchemy.orm import Session

from . import models


def get_projects(db: Session):
    return db.query(models.Project).all()


def get_project(db: Session, slug: str):
    return db.query(models.Project).filter(models.Project.slug == slug).first()
