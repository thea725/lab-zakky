import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    msg = message.payload.decode()
    if msg == "refresh":
        client.publish("slave/master", "0")

client = mqtt.Client()

broker_address = "test.mosquitto.org"
port = 1883
client.connect(broker_address, port)

# Tentukan topik yang akan di-subscribe
topic = "master/slave"

# Set fungsi callback untuk saat pesan diterima
client.on_message = on_message

# Subscribe ke topik
client.subscribe(topic)

# Loop untuk terus menerima pesan
client.loop_forever()