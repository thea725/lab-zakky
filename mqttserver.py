import paho.mqtt.server as mqtt

# Callback saat klien terhubung ke server MQTT
def on_connect(client, userdata, flags, rc):
    print(f"Klien terhubung dengan kode respons: {rc}")

# Callback saat klien mengirim pesan ke topik yang telah diberlangganan
def on_message(client, userdata, message):
    print(f"Pesan diterima pada topik '{message.topic}': {message.payload.decode()}")

# Konfigurasi server MQTT
mqtt_server = mqtt.MQTTv311()
server = mqtt.Server()

# Menghubungkan callback ke server
server.on_connect = on_connect
server.on_message = on_message

# Bind server ke alamat dan port tertentu (ganti dengan alamat dan port yang sesuai)
server.bind("127.0.0.1", 1883)

# Jalankan server dalam mode asinkron
server.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    print("Server MQTT berhenti")
    server.stop()
