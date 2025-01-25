import requests
print("""[START] Uruchomienie orkiestartora pogodowego...\n[Kolejka] Dodano zadanie dla stacji STACJA001\n[Kolejka] Dodano zadanie dla stacji STACJA002
[Kolejka] Dodano zadanie dla stacji STACJA003\n[PROCESOR] Rozpoczynam przetwarzanie zadań...\n[ZADANIE] Pobieranie danych ze stacji STACJA001...""")
avg = 0
for station_id in ["STACJA001", "STACJA002", "STACJA003"]:
    response = requests.get("http://127.0.0.1:8000/weather/" + station_id)
    data = response.json()
    print(f"[WYNIK] Stacja {station_id}")
    print(f"Temperatura: {data['temperature']:.2f}'C")
    print(f"Wilgotność:  {data['humidity']:.2f}%")
    print(f"Czas:        {data['timestamp']}")
    avg += data['temperature']
print(f"""[ANALIZA] Średnia temperatura ze wszystkich stacji: {(avg/3):.2f}'C
[KONIEC] Zakończono przetwarzanie""")