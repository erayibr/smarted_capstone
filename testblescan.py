# test BLE Scanning software
# jcs 6/8/2014

import blescan
import sys
import beacon
import bluetooth._bluetooth as bluez
from rssi_locator import locator
from cleaner import clear
import requests
import json
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ( "192.168.10.101" , 10000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

dev_id = 0

beacon_1 = beacon.beacon("4d6fc88bbe756698da486866a36ec78e")
beacon_2 = beacon.beacon("bc5f638e79976aa42b455a6d5a70128c")
beacon_3 = beacon.beacon("213a8fd53d3fad98b245a8d2b2242a48")

try:
    sock_bluetooth = bluez.hci_open_dev(dev_id)
    print "ble thread started"

except:
    print "error accessing bluetooth device..."
    sys.exit(1)

blescan.hci_le_set_scan_parameters(sock_bluetooth)
blescan.hci_enable_le_scan(sock_bluetooth)




returnedList = blescan.parse_events(sock_bluetooth, 100)

print (returnedList)

try:

    # Send data
    print >>sys.stderr, 'sending message'
    sock.sendall(json.dumps(returnedList))

    # Look for the response
    amount_received = 0
    amount_expected = len(returnedList)
    
    # while amount_received < amount_expected:
    #    data = sock.recv(16)
    #    amount_received += len(data)
    #    print >>sys.stderr, 'received "%s"' % data

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()

    #clear()

    beacon_1.calc()
    beacon_2.calc()
    beacon_3.calc()

    print "beacon_1:", beacon_1.distance
    print "beacon_2:", beacon_2.distance
    print "beacon_3:", beacon_3.distance
       
    x,y = locator(beacon_1.distance, beacon_2.distance, beacon_3.distance, 1.2, 2.35, 0.1, 3.5, 0, 0)    
    print (x,y)
    
    data = {
      "x": x,
      "y": y
    }
    
    #file1 = open("MyFile.txt","w")
    #file1.write('{0}\n{1}\n'.format(x, y))
    #file1.close()
    
    with open('MyFile.txt', 'w') as outfile:
        json.dump(data, outfile)
    
    
    beacon_1.flush()
    beacon_2.flush()
    beacon_3.flush()
