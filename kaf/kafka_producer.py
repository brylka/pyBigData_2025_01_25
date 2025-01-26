from confluent_kafka import Producer
from datetime import datetime

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

    def start_monitoring(self):
        while True:
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

            for station_id in self.monitored_stations:
                message = {
                    'station_id': station_id,
                    'timestamp': timestamp,
                    'action': 'fetch_weather'
                }


if __name__ == "__main__":
    monitor = WeatherStationMonitor()

    for i in range(1,11):
        monitor.add_station(f"STACJA{i:03d}")