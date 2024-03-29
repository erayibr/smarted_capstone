# test BLE Scanning software
# jcs 6/8/2014

import blescan
import bluetooth._bluetooth as bluez
import json
import socket
import sys
import json
import os
from printer import get_angle

dev_id = 0
data = "none"
try:
    sock_bluetooth = bluez.hci_open_dev(dev_id)
    print "ble thread started"

except:
    print "error accessing bluetooth device..."
    sys.exit(1)

blescan.hci_le_set_scan_parameters(sock_bluetooth)
blescan.hci_enable_le_scan(sock_bluetooth)

while True:
    returnedList = blescan.parse_events(sock_bluetooth, 100)
    os.system("cd .. && cd MPU92500/examples/basic-usage/ && sudo python3 measure.py")
    angle = {'rssi': get_angle(), 'uuid': "angle"}
    returnedList.append(angle)
    print(angle)
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ( "192.168.10.101" , 10000)
    print >>sys.stderr, 'connecting to %s port %s' % server_address
    sock.connect(server_address)

    try: 
        # Send data
        print >>sys.stderr, 'sending message'

        sock.sendall(json.dumps(returnedList))
        # print(returnedList)

        # amount_received = 0
        # amount_expected = len(json.dumps(returnedList))
        # print("amount expected: " + str(amount_expected))
        
    finally:
        sock.send(b' ')
        print("before receive")
        sock.settimeout(2)
        try:
            data = sock.recv(256)
        except socket.timeout:
            print("Timed out")
        print("after receive")
        print >>sys.stderr, 'received "%s"' % data
        f = open("audio.txt", "w")
        f.write(data)
        f.close()
        print >>sys.stderr, 'closing socket'
        sock.close()

