from fastapi import FastAPI
from sqlalchemy import MetaData

from . import models

from .schemas import Blog

from .database import engine


metadata = MetaData()
metadata.create_all(bind=engine)

print("Created the table")

app = FastAPI()


@app.post("/blog")
def create(payload: Blog):
    return payload
