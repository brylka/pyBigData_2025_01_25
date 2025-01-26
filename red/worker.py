from redis import Redis
from rq import Queue, SimpleWorker
from rq.timeouts import BaseDeathPenalty


class DummyDeathPenalty(BaseDeathPenalty):
    def setup_death_penalty(self):
        pass
    def cancel_death_penalty(self):
        pass


if __name__ == "__main__":
    redis_conn = Redis()

    queue = Queue('weather_station', connection=redis_conn)
    worker = SimpleWorker([queue], connection=redis_conn)

    worker.death_penalty_class = DummyDeathPenalty

    worker.work()