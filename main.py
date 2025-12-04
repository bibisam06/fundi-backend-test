from fastapi import FastAPI
from typing import Union

#controllers
from controller import items
from controller import users, admins
app = FastAPI()
app.include_router(items.router)
app.include_router(users.router)
app.include_router(admins.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

