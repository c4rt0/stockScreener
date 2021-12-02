import models
import yfinance
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from fastapi import FastAPI, Request, Depends, BackgroundTasks
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from models import Stock

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
def fetch_stock_data(id:int):
    db = SessionLocal()
    stock = db.query(Stock).filter(Stock.id == id).first()
    
    stock.forwardPE = 10
    db.add(stock)
    db.commit()

@app.post("/stock")
async def create_stock(stock_request: StockRequest, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    """
    creates ticker and stores it in the database
    """
    stock = Stock()
    stock.symbol = stock_request.symbol
    
    db.add(stock)
    db.commit()
    
    background_tasks.add_task(fetch_stock_data, stock.id)
    
    return {
        "code":"Success",
        "message":"stock created"
    }