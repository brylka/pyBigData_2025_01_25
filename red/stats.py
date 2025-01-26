from redis import Redis


def show_temp_stats():
    redis_conn = Redis()
    stations = ["STACJA001", "STACJA002", "STACJA003"]

    print(f"=== Statystyki poszczególnych stacji pogodowych ===")
    for station in stations:
        temps = [float(t) for t in redis_conn.lrange(f"temps:{station}", 0, -1)]
        if temps:
            print(f"Stacja: {station}")
            print(f"Liczba pomiarów: {len(temps)}")
            sum = 0
            for temp in temps:
                sum += temp
            av = sum/len(temps)
            print(f"Średnia temperatura: {av:.2f}'C")
            print(f"Największa temperatura: {max(temps):.2f}'C")
            print(f"Najmniejsza temperatura: {min(temps):.2f}'C")


if __name__ == "__main__":
    show_temp_stats()