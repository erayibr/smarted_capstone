import subprocess
import time
import os
import subprocess

file_name_temp = "asdasd"
dirty = 0
while True:
    
    f = open("audio.txt", "r")
    file_name = str(f.read()) + ".wav"
    f.close()
    time.sleep(1)
    print(file_name)

    if ((file_name != file_name_temp) and (file_name != "none.wav")):
        if dirty:
            process.stdin.write('q')
            print("killed: " + file_name_temp)
        dirty = 1
        process = subprocess.Popen(["omxplayer", "-o",  "local",  file_name], stdin=subprocess.PIPE)
        print(file_name)
        print(file_name_temp)
        file_name_temp = file_name
    else:
        continue

    