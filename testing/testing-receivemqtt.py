import paho.mqtt.client as mqtt
from csv import writer
import json

# Fungsi yang akan dipanggil saat pesan diterima
def on_message(client, userdata, message):
    msg = message.payload.decode().replace("\r", "").replace("'",'"')
    obj = json.loads(msg)
    if "msg" in obj:
        print(f"Get message from {message.topic}")
        with open("data.csv", "a", newline='') as file:
            writer_object = writer(file)
            writer_object.writerow(obj["msg"].split(','))
            file.close()
    elif "time" in obj:
        print(f"Transfer time: {obj['time']} milliseconds")

# Inisialisasi MQTT client
client = mqtt.Client()

# Tentukan broker MQTT yang akan digunakan
broker_address = "192.168.137.49"
port = 1883

# Koneksikan ke broker MQTT
client.connect(broker_address, port)

# Tentukan topik yang akan di-subscribe
topic = "slave/master"

# Set fungsi callback untuk saat pesan diterima
client.on_message = on_message

# Subscribe ke topik
client.subscribe(topic)

# Loop untuk terus menerima pesan
client.loop_forever()
