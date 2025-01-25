import requests
from typing import List, Dict

class Task:
    def __init__(self, station_id: str):
        self.station_id = station_id
        self.status = "pending"
        self.result = None

class WeatherOrchestartor:
    def __init__(self):
        self.tasks: List[Task] = []
        self.api_url = "http://127.0.0.1/weather/{station_id}"

    def add_task(self, station_id: str):
        task = Task(station_id)
        self.tasks.append(task)
        print(f"[Kolejka] Dodano zadanie dla stacji {station_id}")


if __name__ == "__main__":
    print("[START] Uruchomienie orkiestartora pogodowego...")
    orchestrator = WeatherOrchestartor()

    stations = ["STACJA001", "STACJA002", "STACJA003"]
    for station in stations:
        orchestrator.add_task(station)

    print("[KONIEC] Zakończono przetwarzanie")