# test BLE Scanning software
# jcs 6/8/2014

import blescan
import sys
import beacon
import bluetooth._bluetooth as bluez

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
    returnedList = blescan.parse_events(sock, 10)
    print "----------"
    for beacon in returnedList:
        print(beacon["uuid"], beacon["rssi"], beacon["distance"])
        
        if(uuid == beacon_1.uuid):
            beacon_1.distance += distance
            beacon_1.count += 1
        elif(uuid == beacon_2.uuid):
            beacon_2.distance += distance
            beacon_2.count += 1
        else:
            beacon_3.distance += distance
            beacon_3.count += 1
            
    beacon1.average()
    beacon2.average()
    beacon3.average()
           
    #location[] = locator(distance_1, distance_2, distance_3, x1, x2, x3, y1, y2, y3)    
#		print beacon
