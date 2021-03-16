import tkinter as tk
import os
import json
 
# Create the window with the Tk class
root = tk.Tk()
root.state('zoomed')
root.title("SMARTED Visitor Tracking Software")
# Create the canvas and make it visible with pack()
canvas = tk.Canvas(root, width=1920, height=1080, highlightthickness=0, relief='ridge')
canvas.pack() # this makes it visible

map = tk.PhotoImage(file="map.png")
canvas.create_image(0, 0, anchor=tk.NW, image=map)

# Loads and create image (put the image in the folder)
img = tk.PhotoImage(file="visitor1.png")
y = 0
x = 0
image = canvas.create_image(x + 53, y + 621, image=img)

def move(event = "none"):
    global x, y
    with open((os.path.dirname(os.getcwd()) + '/Server/coordinates.txt'), 'r') as file:
        data = json.loads(file.read( ))
    canvas.move(image, (data["x"] - x)*160, (y - data["y"])*160)
    x = data["x"]
    y = data["y"]
    root.after(1000, move)
 
# This bind window to keys so that move is called when you press a key
root.after(0, move)
 
# this creates the loop that makes the window stay 'active'
root.mainloop()