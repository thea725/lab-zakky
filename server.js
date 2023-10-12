const aedes = require('aedes')();
const server = require('net').createServer(aedes.handle);

const port = 1883; // Port MQTT default

server.listen(port, function () {
  console.log('MQTT Broker is listening on port', port);
});

aedes.on('client', function (client) {
  console.log('Client connected:', client.id);
});

aedes.on('clientDisconnect', function (client) {
  console.log('Client disconnected:', client.id);
});

aedes.on('publish', function (packet, client) {
  if (client) {
    console.log('Client', client.id, 'published:', packet.payload.toString());
  }
});
