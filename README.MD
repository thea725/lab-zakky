# Zakky Project
Zakky Project is a Python-based MQTT terminal designed to receive messages sent via MQTT broker. The program facilitates communication between nodes or devices connected to a local MQTT broker. These nodes are fed messages from a Raspberry Pi-based feeder, ensuring reliable local connections.

## Overview
The system comprises two main components:

### 1. Feeder (Raspberry Pi)

- The feeder, running a Node.js server (server.js), acts as the MQTT broker.
- It receives messages from various nodes and publishes them to the broker.
- Each node or device is connected locally to the feeder, ensuring robust and efficient communication.

### 2. Terminal (Desktop)

- The Python-based MQTT terminal (desktop.py) is responsible for receiving and displaying messages from the MQTT broker.
- It provides real-time updates on the status of connected nodes, their SD card availability, and their locations.
## Getting Started
### Prerequisites
Before using Zakky Project, ensure the following dependencies are installed:

- Python
- Node.js
## Installation
1. Clone the repository:

```
git clone https://github.com/thea725/lab-zakky.git
cd zakky-project
```

2. Install Python dependencies:

```
pip install -r requirements.txt
```

3. Install Node.js dependencies (on Raspberry Pi):

```
cd raspberry-pi
npm install
```
## Usage
### 1. Desktop Terminal (desktop.py):

- Run the desktop terminal:

```
python desktop.py
```
- Interact with the terminal to start, stop, or check the status of connected nodes.

### 2. Feeder Server (server.js on Raspberry Pi):

- Run the Node.js server:

```
cd raspberry-pi
node server.js
```
- Ensure that the Raspberry Pi has a constant IP address.

### 3. Setting Up Nodes:

- Configure the IP address of each node statically.

- Match the node IP addresses to the relevant edge devices or nodes.
```
# Example for setting a static IP on a Raspberry Pi (replace with your values)
sudo nano /etc/dhcpcd.conf

# Add the following lines at the end of the file:
interface eth0
static ip_address=192.168.1.2/24
static routers=192.168.1.1
static domain_name_servers=192.168.1.1

# Save and exit the editor
sudo reboot
```
### 4. Start the System:

- Power on the nodes and the Node.js server.
- Execute the desktop terminal.
### 5. Check Connection:

- Verify the connection status and data retrieval through the desktop terminal.
### Notes
- It is crucial to maintain a stable Raspberry Pi IP address for seamless communication with nodes.
