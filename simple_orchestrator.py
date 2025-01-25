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
        self.api_url = "http://127.0.0.1:8000/weather/{station_id}"
        #self.url = "http://127.0.0.1:8000/weather/" # tu jeszcze station_id

    def add_task(self, station_id: str):
        task = Task(station_id)
        self.tasks.append(task)
        print(f"[Kolejka] Dodano zadanie dla stacji {station_id}")

    def process_tasks(self):
        print("[PROCESOR] Rozpoczynam przetwarzanie zadań...")

        for task in self.tasks:
            print(f"[ZADANIE] Pobieranie danych ze stacji {task.station_id}...")
            response = requests.get(self.api_url.format(station_id=task.station_id))
            #response = requests.get(self.url + str(task.station_id))
            data = response.json()

            task.result = data

            print(f"[WYNIK] Stacja {task.station_id}")
            print(f"Temperatura: {data['temperature']:.2f}'C")
            print(f"Wilgotność:  {data['humidity']:.2f}%")
            print(f"Czas:        {data['timestamp']}")


if __name__ == "__main__":
    print("[START] Uruchomienie orkiestartora pogodowego...")
    orchestrator = WeatherOrchestartor()

    stations = ["STACJA001", "STACJA002", "STACJA003"]
    for station in stations:
        orchestrator.add_task(station)

    orchestrator.process_tasks()

    print("[KONIEC] Zakończono przetwarzanie")