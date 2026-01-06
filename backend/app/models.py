from sqlalchemy import Column, Integer, String, Text

from .database import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    slug = Column(String, unique=True, index=True)
    title = Column(String)
    description = Column(Text)
    image = Column(String)
    tags = Column(String)  # comma separated
    details = Column(Text)
