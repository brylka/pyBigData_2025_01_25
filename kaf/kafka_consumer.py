from confluent_kafka import Consumer


class WeatherDataConsumer:
    def __init__(self):
        conf = {
            'bootstrap.servers': 'localhost:9092',
            'group.id': 'weather_data',
            'auto.offset.reset': 'latest'
        }
        self.consumer = Consumer(conf)
        print(f"Konsument zainicjowany")

    def start_consuming(self):
        while True:
            pass


if __name__ == "__main__":
    consumer = WeatherDataConsumer()
    consumer.start_consuming()