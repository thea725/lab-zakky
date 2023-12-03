import requests

esp32_ip = "192.168.137.234"  # Replace with the actual IP of your ESP32
url = f"http://{esp32_ip}/data"

response = requests.get(url)
if response.status_code == 200:
    with open("received_data.csv", "wb") as file:
        file.write(response.content)
    print("Data received successfully.")
else:
    print("Failed to receive data.")
