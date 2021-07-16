import subprocess
import time
import subprocess

file_name_temp = "asdasd"
dirty = 0
while True:
    
    f = open("audio.txt", "r")
    file_name = str(f.read()) + ".wav"
    f.close()
    time.sleep(1)
    # print(file_name)

    if (file_name != file_name_temp):
        if dirty and process.poll() == None:
            process.stdin.write('q')
            print("killed: " + file_name_temp)
        dirty = 1
        if file_name != "none.wav":
            process = subprocess.Popen(["omxplayer", "-o",  "local",  file_name], stdin=subprocess.PIPE)
        # print(file_name)
        # print(file_name_temp)
        file_name_temp = file_name
    else:
        continue

    