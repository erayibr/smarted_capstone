import socket
import sys
import sys
import beacon
from rssi_locator import locator
from cleaner import clear
import json

beacon_1 = beacon.beacon("4d6fc88bbe756698da486866a36ec78e")
beacon_2 = beacon.beacon("bc5f638e79976aa42b455a6d5a70128c")
beacon_3 = beacon.beacon("213a8fd53d3fad98b245a8d2b2242a48")

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('192.168.10.101', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)       

# Listen for incoming connections
sock.listen(1)

data = ""

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()

    try:
        print >>sys.stderr, 'connection from', client_address

        # Receive the data in small chunks and retransmit it
        while True:
            chunk = connection.recv(1024)
            data = data + chunk
            if chunk:
                print >>sys.stderr, 'sending data back to the client'
                #connection.sendall(data)
            else:
                print >>sys.stderr, 'no more data from', client_address
                break
            
    finally:
        # Clean up the connection
        data = json.loads(data)
        print(data)
        connection.close()
            
    for beacon in data:
        #print(beacon["uuid"], beacon["rssi"], beacon["distance"])
        
        if(beacon["uuid"] == beacon_1.uuid):
            beacon_1.rssi.append(beacon['rssi'])
        elif(beacon["uuid"] == beacon_2.uuid):
            beacon_2.rssi.append(beacon['rssi'])
        elif(beacon["uuid"] == beacon_3.uuid):
            #print(beacon['rssi'])
            beacon_3.rssi.append(beacon['rssi'])

    beacon_1.calc()
    beacon_2.calc()
    beacon_3.calc()

    print "beacon_1:", beacon_1.distance
    print "beacon_2:", beacon_2.distance
    print "beacon_3:", beacon_3.distance