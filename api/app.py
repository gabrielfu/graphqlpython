import uvicorn
from fastapi import APIRouter, Depends, FastAPI
from db import init_db, db_session

app = FastAPI()
app.debug = True

@app.on_event("startup")
def startup():
    init_db()

@app.on_event("shutdown")
def shutdown():
    db_session.remove()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)