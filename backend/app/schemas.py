from pydantic import BaseModel


class ProjectBase(BaseModel):
    slug: str
    title: str
    description: str
    image: str
    tags: str
    details: str


class Project(ProjectBase):
    id: int

    class Config:
        orm_mode = True
