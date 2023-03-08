from fastapi import FastAPI
from routers import file, admin, auth, client, dashboard
from db import models, database
import uvicorn

app = FastAPI()

app.include_router(file.router)
app.include_router(auth.router)
app.include_router(admin.router)
app.include_router(client.router)
app.include_router(dashboard.router)

models.Base.metadata.create_all(bind=database.engine)


@app.get("/")
def home():
    return {"message": "navigate to /docs for full documentation"}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
