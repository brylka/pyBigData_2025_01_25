import json
from confluent_kafka import Consumer, KafkaError
from red.tasks import fetch_weather_data

class WeatherDataConsumer:
    def __init__(self):
        conf = {
            'bootstrap.servers': 'localhost:9092',
            'group.id': 'weather_data',
            'auto.offset.reset': 'latest'
        }
        self.consumer = Consumer(conf)
        self.consumer.subscribe(['weather_data'])
        print(f"Konsument zainicjowany")

    def start_consuming(self):
        while True:
            msg = self.consumer.poll(1.0)

            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(f"Błąd: {msg.error()}")
                    break

            data = json.loads(msg.value().decode("utf-8"))
            station_id = data['station_id']
            print(f"Otrzymano zadanie dla stacji: {station_id}")

            weather_data = fetch_weather_data(station_id, False)
            if weather_data:
                temperature = weather_data['temperature']
                timestamp = weather_data['timestamp']
                print(f"Stacja {station_id} temperatura: {temperature:.2f}'C timestamp: {timestamp}")

if __name__ == "__main__":
    consumer = WeatherDataConsumer()
    consumer.start_consuming()