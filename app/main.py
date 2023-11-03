from fastapi import FastAPI
from app.database.session import get_db
from app.routers import url

app = FastAPI()

app.include_router(url.router)
