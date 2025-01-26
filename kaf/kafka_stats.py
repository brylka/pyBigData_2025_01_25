import pandas as pd


def show_stats():
    try:
        df = pd.read_csv("weather_data.csv")

        grouped = df.groupby("station_id")

        for station_id, group in grouped:
            print(f"=== Statystyki dla stacji {station_id} ===")
            print(f"Liczba pomiarów: {len(group)}")
            print(f"Średnia temperatura:     {group['temperature'].mean():.2f}'C")
            print(f"Największa temperatura:  {group['temperature'].max():.2f}'C")
            print(f"Najmniejsza temperatura: {group['temperature'].min():.2f}'C")
    except Exception as e:
        print(f"Problem z pobraniem danych: {e}")


if __name__ == "__main__":
    show_stats()