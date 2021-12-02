import models
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    """
    Present the stock screener dashboard
    """
    return templates.TemplateResponse("home.html", {
        "request":request
        # "someVar": 'BTC'
        })

@app.post("/stock")
def create_stock():
    """
    creates ticker and stores it in the database
    """
    return {
        "code":"Success",
        "message":"stock created"
    }