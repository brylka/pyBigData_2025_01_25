import random
from datetime import datetime
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/weather/{station_id}")
def get_weather_simple(station_id: str):
    return {
        "station_id": station_id,
        "temperature": random.uniform(-15, 45),
        "humidity": random.uniform(40,80),
        "timestamp": datetime.now()
    }


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)