import PySimpleGUI as sg
import paho.mqtt.client as mqtt
import datetime
import json
from time import sleep

# initialize broker server
broker_addr = "test.mosquitto.org" # sg.popup_get_text('MQTT Broker: ', default_text='test.mosquitto.org')
broker_port = 1883 # int(sg.popup_get_text('MQTT Broker: ', default_text='1883'))
client = mqtt.Client()
client.connect(broker_addr, broker_port)

def time():
    waktu = datetime.datetime.now()
    return f"{waktu.hour}:{waktu.minute}:{waktu.second}"
def on_message(client, userdata, message):
    msg = message.payload.decode().replace("'", '"')
    data = json.loads(msg)

    if "loc" in data:
        node_status[int(data["node_id"])] = "1"
        node_sd[int(data["node_id"])] = data["sd"]
        node_loc[int(data["node_id"])] = data["loc"]
        for i in range(16):
            popup_window[f"-TEXT{i+1}-"].update("Connected" if node_status[i+1]=="1" else "Disconnected")
            popup_window[f"-SDTEXT{i+1}-"].update("SD Ready" if node_sd[i+1]=="1" else "SD Failure")
            popup_window[f"-LOCTEXT{i+1}-"].update(node_loc[i+1])

client.on_message = on_message

refresh_time = time()
node_status = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
node_sd = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
node_loc = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]

# Layout components
lay_addr = sg.Column([
    [sg.Frame("Broker Address:", [[sg.Text(f"{broker_addr}:{broker_port}")]])]
])
lay_log = sg.Column([
    [sg.Frame("Log:", [[sg.Multiline('', size=(50, 10), key='-LOG-', autoscroll=True)]], k="-LOG-")]
])
lay_logging = sg.Column([
    [sg.Frame("Actions",[[sg.Button("Start", k="-START-"), sg.Button("Stop", k="-STOP-")]])]
])
lay_status = sg.Column([
    [sg.Frame("Node Status",[[sg.Button("Show", k="-STATUS-")]])]
])
lay_graph = sg.Column([
    [sg.Frame("Graph", [[sg.Button("Show", k="-GRAPH-")]])]
])

layout = [
    [lay_addr, lay_status, lay_logging],
    [lay_log],
    [lay_graph]
]

window = sg.Window("MQTT Terminal", layout, finalize=True)

client.subscribe("slave/master")
client.loop_start()

# Loop utama
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    # Fungsi Tombol
    elif event == "-START-":
        window["-LOG-"].print(f"Start Time: {time()}")
        client.publish("master/slave", "A")
    elif event == "-STOP-":
        window["-LOG-"].print(f"Stop Time: {time()}")
        client.publish("master/slave", "s")
    # Status Window
    elif event == "-STATUS-":
        lay_stats = []
        for i in range(16):
            lay_stats.append([sg.Text(f"Node {i+1}:\t"),
                                sg.Text("Connected" if node_status[i+1]=="1" else "Disconnected", k=f"-TEXT{i+1}-"),
                                sg.Text("SD Ready" if node_sd[i+1]=="1" else "SD Failure", k=f"-SDTEXT{i+1}-"),
                                sg.Text(f"{node_loc[i+1]}", k=f"-LOCTEXT{i+1}-")])
        layout_status = [
            [sg.Text("Waktu Update:"), sg.Text(refresh_time, k="-WAKTU-")],
            lay_stats,
            [sg.Button("Sync", k="-SYNC-")]
        ]
        popup_window = sg.Window('Node Status', layout_status)

        while True:
            popup_event, popup_values = popup_window.read()

            if popup_event == sg.WIN_CLOSED:
                break
            elif popup_event == "-SYNC-":
                client.publish("master/slave", "sync")

                #loop 16x
                for i in range(16):
                    node_status[i] = "0"
                    node_sd[i] = "0"
                    node_loc[i] = "0"
                refresh_time = time()
                popup_window["-WAKTU-"].update(refresh_time)

        popup_window.close()
    elif event == "-GRAPH-":
        lay_graph = []
        for i in range(16):
            lay_graph.append([sg.Text(f"Node {i+1}"),
                                sg.Button("Show", k=f"-SHOW{i+1}-")])
        layout_graph = [
            [sg.Button("Grab", k="-GRAB-"), sg.Button("Reset", k="-RESET-")],
            lay_graph
        ]
        graph_window = sg.Window("Graph Window", layout_graph)

        while True:
            graph_event, graph_value = graph_window.read()
            if graph_event == sg.WIN_CLOSED:
                break
            elif graph_event == "-GRAB-":
                client.publish("master/slave", "P")
            elif graph_event == "-RESET-":
                client.publish("master/slave", "R")

# Tutup koneksi MQTT dan keluar
window.close()