# test BLE Scanning software
# jcs 6/8/2014

import blescan
import sys
import beacon
import bluetooth._bluetooth as bluez
from rssi_locator import locator
import requests
import json

dev_id = 0


beacon_1 = beacon.beacon("4d6fc88bbe756698da486866a36ec78e")
beacon_2 = beacon.beacon("bc5f638e79976aa42b455a6d5a70128c")
beacon_3 = beacon.beacon("213a8fd53d3fad98b245a8d2b2242a48")

try:
    sock = bluez.hci_open_dev(dev_id)
    print "ble thread started"

except:
    print "error accessing bluetooth device..."
    sys.exit(1)

blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock)



while True:
    returnedList = blescan.parse_events(sock, 40)
    print "----------"
    for beacon in returnedList:
        #print(beacon["uuid"], beacon["rssi"], beacon["distance"])
        
        if(beacon["uuid"] == beacon_1.uuid):
            beacon_1.distance += beacon["distance"]
            beacon_1.count += 1
        elif(beacon["uuid"] == beacon_2.uuid):
            beacon_2.distance += beacon["distance"]
            beacon_2.count += 1
        else:
            beacon_3.distance += beacon["distance"]
            beacon_3.count += 1
            
    print "beacon_1:", beacon_1.average()
    print "beacon_2:", beacon_2.average()
    print "beacon_3:", beacon_3.average()
       
    x,y = locator(beacon_1.distance, beacon_2.distance, beacon_3.distance, 2.6, 2.35, 0.1, 3.5, 0, 0)    
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
