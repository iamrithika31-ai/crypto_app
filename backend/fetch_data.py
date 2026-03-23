from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
import requests

# ===============================
# Database setup
# ===============================
DATABASE_URL = "sqlite:///./crypto.db"  # or your preferred DB
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# ===============================
# MarketData table
# ===============================
class MarketData(Base):
    __tablename__ = "market_data"
    __table_args__ = {'extend_existing': True} 

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, index=True)
    price = Column(Float)
    volume = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

# ===============================
# Create tables
# ===============================
Base.metadata.create_all(bind=engine)

# ===============================
# Function to fetch & store market data
# ===============================
def fetch_and_store(symbol: str = "BTC"):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol.lower()}&vs_currencies=usd&include_24hr_vol=true"
    response = requests.get(url)
    data = response.json()

    price = data[symbol.lower()]["usd"]
    volume = data[symbol.lower()]["usd_24h_vol"]

    db = SessionLocal()
    market_entry = MarketData(symbol=symbol.upper(), price=price, volume=volume)
    db.add(market_entry)
    db.commit()
    db.refresh(market_entry)
    db.close()

    return market_entry