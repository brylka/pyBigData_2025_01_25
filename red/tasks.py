import requests

station_id = 'STACJA001'

print(f"Pobieranie danych dla stacji {station_id}...")

response = requests.get(f"http://127.0.0.1:8000/weather/{station_id}")

data = response.json()
print(data)