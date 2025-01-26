import requests


def fetch_weather_data(station_id: str):
    try:
        print(f"Pobieranie danych dla stacji {station_id}...")

        response = requests.get(f"http://127.0.0.1:8000/weather/{station_id}")

        if response.status_code == 200:
            data = response.json()
            temp = data["temperature"]
            if temp > 30:
                print(f"Wysoka temperatura {temp}'C na stacji {station_id}")
            return data
        else:
            print(f"Błąd: {response.status_code}")
            # obsługa błędów
            return None
    except Exception as e:
        print(f"Błąd: {e}")
        # obsługa błędów
        return None


print(fetch_weather_data("STACJA001"))