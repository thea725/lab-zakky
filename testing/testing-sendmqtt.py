import paho.mqtt.client as mqtt

# Konfigurasi broker MQTT
mqtt_broker = "test.mosquitto.org"
mqtt_port = 1883
mqtt_topic = "master/slave"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Terhubung ke broker MQTT")
    else:
        print("Gagal terhubung ke broker MQTT, kode: " + str(rc))

def on_publish(client, userdata, mid):
    print("Pesan terkirim")

client = mqtt.Client()
client.on_connect = on_connect
client.on_publish = on_publish

client.connect(mqtt_broker, mqtt_port, keepalive=60)

# Kirim pesan "s" ke topik MQTT
pesan = "100"
client.publish(mqtt_topic, pesan)

# Tunggu pesan terkirim
client.loop_forever()
