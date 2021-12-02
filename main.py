import models
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

class StockRequest(BaseModel):
    symbol: str

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

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
def create_stock(stock_request: StockRequest):
    """
    creates ticker and stores it in the database
    """
    return {
        "code":"Success",
        "message":"stock created"
    }