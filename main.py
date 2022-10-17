from fastapi import FastAPI
from db import Database

app = FastAPI()
db = Database('data.db')

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/url/{name}")
async def say_hello(name: str):
    db.add_user(name)
    return {"message": f"Hello {name}"}
