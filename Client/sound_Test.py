import subprocess
import time
import json

while True:
    with open('audio.txt') as f:
        file_name = json.load(f) + ".wav"

    process_id = subprocess.Popen(["omxplayer", "-o",  "local",  file_name])
    print("test")
    process_id.wait()