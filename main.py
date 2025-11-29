from fastapi import FastAPI
from typing import Union

#controllers
from controller import items
from controller import users
app = FastAPI()
app.include_router(items.router)
app.include_router(users.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

