from app.database import Base, engine
from app.routers import projects
from fastapi import FastAPI

app = FastAPI(title="Sohail Portfolio API")

Base.metadata.create_all(bind=engine)

app.include_router(projects.router)


@app.get("/")
def health():
    return {"status": "Portfolio API running"}
