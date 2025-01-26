from confluent_kafka import Producer


class WeatherStationMonitor:
    def __init__(self):
        conf = {
            'bootstrap.servers': 'localhost:9092'
        }
        self.producer = Producer(conf)
        self.monitored_stations = set()

    def add_station(self, station_id):
        self.monitored_stations.add(station_id)
        print(f"Dodano stację: {station_id}")


if __name__ == "__main__":
    monitor = WeatherStationMonitor()

    for i in range(1,11):
        monitor.add_station(f"STACJA{i}")