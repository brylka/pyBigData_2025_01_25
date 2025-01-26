from redis import Redis
from rq import Queue

class WeatherStationMonitor:
    def __init__(self):
        print(f"Start monitora")
        self.redis_conn = Redis()
        self.queue = Queue('weather_ststion', connection=self.redis_conn)


monitor = WeatherStationMonitor()