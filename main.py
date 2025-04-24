import sqlite3
import os
from fastapi import FastAPI, HTTPException, Depends
from typing import Annotated, List
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import SessionLocal, engine
import models
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Get the frontend URL from environment variable or use default
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:3000")

origins = [
    FRONTEND_URL,
    "http://localhost:3000",
    "https://your-vercel-app-url.vercel.app"  # Replace with your actual Vercel URL
]

app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

class CampaignBase(BaseModel):
    name: str
    status: str
    clicks: int
    cost: float
    impressions: int

class CampaignModel(CampaignBase):
   id: int
   class Config:
      orm_mode= True


def get_db():
    db = SessionLocal()
    try:
      yield db
    finally:
      db.close()

db_dependency = Annotated[Session, Depends(get_db)]
models.Base.metadata.create_all(bind=engine)


@app.get("/campaigns", response_model=List[CampaignModel])
async def read_campaigns(db: db_dependency, skip: int=0, limit: int= 100):
   campaigns=db.query(models.Campaigns).offset(skip).limit(limit).all()
   return campaigns


@app.on_event("startup")
def startup_populate_mock_data():
    conn = sqlite3.connect('./campaign.db')
    cursor = conn.cursor()

  
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS campaigns (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            status TEXT NOT NULL,
            clicks INTEGER NOT NULL,
            cost REAL NOT NULL,
            impressions INTEGER NOT NULL
        );
    ''')

    
    cursor.execute("SELECT COUNT(*) FROM campaigns")
    count = cursor.fetchone()[0]

    if count == 0:
        
        cursor.executemany('''
            INSERT INTO campaigns (name, status, clicks, cost, impressions) VALUES (?, ?, ?, ?, ?)
        ''', [
            ('Summer Sale', 'Active', 150, 45.99, 1000),
            ('Black Friday', 'Paused', 320, 89.50, 2500),
            ('Holiday Blast', 'Active', 210, 67.80, 1800),
            ('Winter Warmers', 'Paused', 90, 30.00, 1200),
            ('Spring Launch', 'Active', 180, 55.20, 1400),
            ('New Year Promo', 'Paused', 250, 72.40, 2300),
            ('Flash Deals', 'Active', 300, 95.00, 2700),
            ('Daily Steals', 'Active', 125, 42.10, 1100),
            ('Festival Dhamaka', 'Active', 200, 60.00, 1600),
            ('Clearance Sale', 'Paused', 175, 50.75, 1500)
        ])
        conn.commit()

    conn.close()

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
