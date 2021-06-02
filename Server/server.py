import socket
import sys
import beacon
from rssi_locator import locator
from cleaner import clear
import json
import time

beacon_1 = beacon.beacon("4d6fc88bbe756698da486866a36ec78e" , 1.25, 3.5)
beacon_2 = beacon.beacon("bc5f638e79976aa42b455a6d5a70128c", 1.25, 0)
beacon_3 = beacon.beacon("213a8fd53d3fad98b245a8d2b2242a48", 3.25, 1.25)
beacon_4 = beacon.beacon("6f506cd2e98121a7a5493da8fcca68d6", 2.75, 3.5)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('192.168.2.128', 10000)
print('starting up on %s port %s' % server_address, file=sys.stderr)
sock.bind(server_address)       

# Listen for incoming connections
sock.listen(1)
connection_number = 1

while True:
    message = b""
    # Wait for a connection
    print('waiting for a connection', file=sys.stderr)
    connection, client_address = sock.accept()

    try:
        print('connection from', client_address, file=sys.stderr)
        time_start = round(time.time() * 1000)

        # Receive the data in small chunks and retransmit it
        while True:
            chunk = connection.recv(1024)
            message = message + chunk
            # print("recv")
            if (chunk == b' '):
                print("entered")
                break
        
        
                
    finally:
        print("in finally:")
        message = json.loads(message)
        # Clean up the connection
        for beacon in message:
            #print(beacon["uuid"], beacon["rssi"], beacon["distance"])
            if(beacon["uuid"] == beacon_1.uuid):
                beacon_1.rssi.append(beacon['rssi'])
            elif(beacon["uuid"] == beacon_2.uuid):
                beacon_2.rssi.append(beacon['rssi'])
            elif(beacon["uuid"] == beacon_3.uuid):
                #print(beacon['rssi'])
                beacon_3.rssi.append(beacon['rssi'])
            elif(beacon["uuid"] == beacon_4.uuid):
                #print(beacon['rssi'])
                beacon_4.rssi.append(beacon['rssi'])
            elif(beacon["uuid"] == "angle"):
                angle = beacon['rssi']
            
        beacon_1.calc()
        beacon_2.calc()
        beacon_3.calc()
        beacon_4.calc()

        best3= []
        best3.append(beacon_1)
        best3.append(beacon_2)
        best3.append(beacon_3)
        best3.append(beacon_4)
        best3.sort(key=lambda x: x.distance, reverse=True)

        x,y = locator(best3[3].distance, best3[1].distance, best3[2].distance, best3[3].pos_x, best3[1].pos_x, best3[2].pos_x, best3[3].pos_y, best3[1].pos_y, best3[2].pos_y)    
        
        for beacon in best3:
            if beacon.distance < 1.25:
                file_name = beacon.uuid
                break
            else:
                file_name = "none"
        
        #print(message)
        print("sending")
        connection.sendall(bytes(file_name, 'UTF-8'))
        connection.close()


    # time_start_proc = round(time.time() * 1000)        
    
    # print((x,y))

    data = {"x": x, "y": y, "beacon_1": beacon_1.distance, "beacon_2": beacon_2.distance, "beacon_3": beacon_3.distance , "beacon_4": beacon_4.distance, "angle": angle }

    # time_end = round(time.time() * 1000)
    # print("The total time required for a server response in connection " + str(connection_number) + " is: " + str(time_end - time_start) + "ms")
    # print("The processing time for a single device in connection " + str(connection_number) + " is: " + str(time_end - time_start_proc) + "ms")
    # connection_number = connection_number + 1
    beacon_1.flush()
    beacon_2.flush()
    beacon_3.flush()
    beacon_4.flush()

    with open('data.txt', 'w') as file:
        file.write(json.dumps(data))