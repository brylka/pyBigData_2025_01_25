from redis import Redis
from rq import Queue
import time
from datetime import datetime
from tasks import fetch_weather_data

class WeatherStationMonitor:
    def __init__(self):
        print(f"Start monitora")
        self.redis_conn = Redis()
        self.queue = Queue('weather_ststion', connection=self.redis_conn)
        self.monitored_stations = set()

    def add_station(self, station_id):
        self.monitored_stations.add(station_id)
        print(f"Dodano stację: {station_id}")

    def start_monitoring(self):
        while True:

            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

            for station_id in self.monitored_stations:
                job = self.queue.enqueue(
                    fetch_weather_data,
                    station_id,
                    job_id=f"weather_{station_id}_{timestamp}",
                    job_timeout="5m"
                )
                print(f"Dodano zadanie: {job.id}")

            time.sleep(30)
if __name__ == "__main__":
    monitor = WeatherStationMonitor()
    monitor.add_station("STACJA001")
    monitor.add_station("STACJA002")
    monitor.add_station("STACJA003")
    monitor.start_monitoring()