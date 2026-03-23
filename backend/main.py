from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base   
from models import MarketData                     
from fetch_data import fetch_and_store            
from analytics import compute_analytics           
from strategy import simple_strategy              
import pandas as pd

app = FastAPI(title="Crypto Market API")

# CORS (for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ----------------------
# Fetch Data
# ----------------------
@app.post("/fetch")
def fetch():
    fetch_and_store()
    return {"message": "Data fetched"}

# ----------------------
# Market APIs
# ----------------------
@app.get("/markets")
def markets(db: Session = Depends(get_db)):
    return db.query(MarketData).all()

@app.get("/prices")
def prices(symbol: str, db: Session = Depends(get_db)):
    return db.query(MarketData).filter(MarketData.symbol == symbol.upper()).all()

@app.get("/history")
def history(symbol: str, limit: int = 50, db: Session = Depends(get_db)):
    return db.query(MarketData)\
        .filter(MarketData.symbol == symbol.upper())\
        .order_by(MarketData.timestamp.desc())\
        .limit(limit)\
        .all()

# ----------------------
# Analytics
# ----------------------
@app.get("/analytics")
def analytics_api(db: Session = Depends(get_db)):
    data = db.query(MarketData).all()

    df = pd.DataFrame([{
        "symbol": d.symbol,
        "price": d.price,
        "volume": d.volume,
        "timestamp": d.timestamp
    } for d in data])

    return compute_analytics(df)

# ----------------------
# Strategy
# ----------------------
@app.post("/strategy/run")
def strategy_api(db: Session = Depends(get_db)):
    data = db.query(MarketData).all()

    df = pd.DataFrame([{
        "symbol": d.symbol,
        "price": d.price,
        "timestamp": d.timestamp
    } for d in data])

    return simple_strategy(df)