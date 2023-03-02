from fastapi import FastAPI
from routers import file, admin, auth, client
from db import models, database

app = FastAPI()

app.include_router(file.router)
app.include_router(auth.router)
app.include_router(admin.router)
app.include_router(client.router)

models.Base.metadata.create_all(bind=database.engine)


@app.get("/")
def home():
    return {"message": "navigate to /docs for full documentation"}
