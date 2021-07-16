import socket
import sys
import beacon
from rssi_locator import locator
from cleaner import clear
import json
import time

beacon_1 = beacon.beacon("4d6fc88bbe756698da486866a36ec78e" , 1.0, 3.5, 90, "Carvaggio")
beacon_2 = beacon.beacon("bc5f638e79976aa42b455a6d5a70128c", 1.0, 0.0, -90, "Saint Remy")
beacon_3 = beacon.beacon("213a8fd53d3fad98b245a8d2b2242a48", 2.5, 0.0, -90, "Mona Lisa")
beacon_4 = beacon.beacon("6f506cd2e98121a7a5493da8fcca68d6", 2.5, 3.5, 90, "Last Supper")
beacon_5 = beacon.beacon("fb6e46120f6720812444a02997a07bce", 4.2, 3.5, 90, "Starry Night")
beacon_6 = beacon.beacon("4d3cee80e9b2d1a8e54fad2d9681861e", 5.2, 3.5, 90, "Potato Eaters")
beacon_7 = beacon.beacon("efb9f2968412bd96a64874103329ea81", 2.6, 4.3, 180, "Introduction - Girl With a Pearl Earring")

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('192.168.10.101', 10000)
print('starting up on %s port %s' % server_address, file=sys.stderr)
sock.bind(server_address)       

# Listen for incoming connections
sock.listen(1)
connection_number = 1
file_name_counter = 0

while True:
    message = b""
    # Wait for a connection
    print('waiting for a connection', file=sys.stderr)
    connection, client_address = sock.accept()

    try:
        print('connection from', client_address, file=sys.stderr)
        time_start = round(time.time() * 1000)
        counter = 0;
        # Receive the data in small chunks and retransmit it
        while True:
            print("received")
            chunk = connection.recv(256)
            message = message + chunk
            counter = counter + 1
            # print("recv")
            if (chunk == b' ') or counter > 50:
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
            elif(beacon["uuid"] == beacon_5.uuid):
                #print(beacon['rssi'])
                beacon_5.rssi.append(beacon['rssi'])
            elif(beacon["uuid"] == beacon_6.uuid):
                #print(beacon['rssi'])
                beacon_6.rssi.append(beacon['rssi'])
            elif(beacon["uuid"] == beacon_7.uuid):
                #print(beacon['rssi'])
                beacon_7.rssi.append(beacon['rssi'])
            elif(beacon["uuid"] == "angle"):
                angle = float(beacon['rssi'])
            
        beacon_1.calc()
        beacon_2.calc()
        beacon_3.calc()
        beacon_4.calc()
        beacon_5.calc()
        beacon_6.calc()
        beacon_7.calc()

        best3= []
        best3.append(beacon_1)
        best3.append(beacon_2)
        best3.append(beacon_3)
        best3.append(beacon_4)
        best3.append(beacon_5)
        best3.append(beacon_6)
        best3.append(beacon_7)
        best3.sort(key=lambda x: x.distance, reverse=False)
        print(best3[0].distance)
        
        if((best3[0].uuid == beacon_5.uuid) or (best3[0].uuid == beacon_6.uuid) or (best3[0].uuid == beacon_7.uuid)):
            room = 2
        else:
            room = 1

        x,y = locator(best3[0].calc_default(), best3[1].calc_default(), best3[2].calc_default(), best3[0].pos_x, best3[1].pos_x, best3[2].pos_x, best3[0].pos_y, best3[1].pos_y, best3[2].pos_y, room)    
    
        if (best3[0].distance < 1.2) and (best3[0].angle_check(angle)):
            file_name_temp = best3[0].uuid
            audio_file_temp = best3[0].audio_file
        else:
            file_name_temp = "none"
            audio_file_temp = "none"

        if(file_name_counter == 0):
            file_name = file_name_temp
            audio_file = audio_file_temp
            file_name_counter = 3
        elif ((file_name_counter != 0) and (file_name != file_name_temp)):
            file_name_counter = file_name_counter - 1
        elif (file_name == file_name_temp):
            file_name_counter = min(3, file_name_counter + 1)

        #print(message)
        print("sending")
        connection.settimeout(2)
        try:
            print("sendall")
            connection.sendall(bytes(file_name, 'UTF-8'))
        except connection.timeout:
            print("time out")
        connection.close()


    # time_start_proc = round(time.time() * 1000)        
    
    # print((x,y))

    data = {"x": x, "y": y, "beacon_1": beacon_1.distance, "beacon_2": beacon_2.distance, "beacon_3": beacon_3.distance , "beacon_4": beacon_4.distance, "beacon_5": beacon_5.distance, "beacon_6": beacon_6.distance, "beacon_7": beacon_7.distance, "angle": angle, "room": room, "audio": audio_file}

    # time_end = round(time.time() * 1000)
    # print("The total time required for a server response in connection " + str(connection_number) + " is: " + str(time_end - time_start) + "ms")
    # print("The processing time for a single device in connection " + str(connection_number) + " is: " + str(time_end - time_start_proc) + "ms")
    # connection_number = connection_number + 1
    beacon_1.flush()
    beacon_2.flush()
    beacon_3.flush()
    beacon_4.flush()
    beacon_5.flush()
    beacon_6.flush()
    beacon_7.flush()

    with open('data.txt', 'w') as file:
        file.write(json.dumps(data))