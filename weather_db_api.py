import random
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI
import uvicorn

app = FastAPI()

DB_URL = "mysql+mysqlconnector://root:@localhost/qwer"
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class WeatherData(Base):
    __tablename__ = "weather"
    id = Column(Integer, primary_key=True, index=True)
    city = Column(String(100))
    temperature = Column(Float)
    humidity = Column(Float)
    timestamp = Column(DateTime, default=datetime.now)

Base.metadata.create_all(bind=engine)

@app.get("/weather/{city}")
def get_weather_simple(city: str):
    db = SessionLocal()
    last_weather = (db.query(WeatherData)
            .filter(WeatherData.city == city)
            .order_by(WeatherData.timestamp.desc())
            .first())
    db.close()


    return {
        "city": last_weather.city,
        "temperature": last_weather.temperature,
        "humidity": last_weather.humidity,
        "timestamp": str(last_weather.timestamp)
    }


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)