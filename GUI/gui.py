import tkinter as tk
import os
import json
import tkinter.messagebox
import re
import random
import math
import numpy as np

# Create the window with the Tk class
root = tk.Tk()
root.state('zoomed')
root.title("SMARTED Visitor Tracking Software")
root.minsize(width = 1400, height = 800)

mainframe=tk.Frame(root).pack()
#to manage the right of the screen
Offset_y=400    #offset from top
Offset_x=-80     #offset from left


# Create the canvas and make it visible with pack()
canvas = tk.Canvas(mainframe, width=1920, height=1080, highlightthickness=0, relief='ridge')
canvas.place(x=0, y=0) # this makes it visible

map = tk.PhotoImage(file="map.png")
canvas.create_image(0, 0, anchor=tk.NW, image=map)

# Loads and create image (put the image in the folder)
img = tk.PhotoImage(file="visitor1.png")
image = canvas.create_image(0, 0, image=img)
arrow_1 = canvas.create_line(0, 0, 0, 0, arrow=tk.LAST, fill='red', width= '4')  

def move(event = "none"):
    global x, y
    with open((os.path.dirname(os.getcwd()) + '/Server/data.txt'), 'r') as file:
        data = json.loads(file.read( ))
    angle = data["angle"]
    x = data["x"]
    y = data["y"]
    x_image = 40 + data["x"]*152    #160 pixel for 1 meter, 95% resized
    y_image = 740 -(data["y"])*152  #160 pixel for 1 meter, 95% resized
    arrow_length = 100
    canvas.coords(image, x_image, y_image)
    canvas.coords(arrow_1, x_image , y_image , arrow_length*math.cos(-angle*np.pi/180)+x_image , arrow_length*math.sin(-angle*np.pi/180) + y_image)

    coordinates = "Location (m):    x=" + " {:2.2f}     ".format(x) + "y=" + " {:2.2f} ".format(y)
    coordinates_label.config(text = coordinates)

    angle = "Angle (degree): " + " {:2.2f}     ".format(angle)
    angle_label.config(text = angle)

    beacons = "Distance to Beacons (m):    b1=" + " {:2.2f}     ".format(data["beacon_1"]) + "b2=" + " {:2.2f}     ".format(data["beacon_2"]) + "b3=" + " {:2.2f}     ".format(data["beacon_3"]) + "b4=" + " {:2.2f}     ".format(data["beacon_4"])     + "b5=" + " {:2.2f}     ".format(data["beacon_5"]) + "b6=" + " {:2.2f}     ".format(data["beacon_6"]) + "b7=" + " {:2.2f}     ".format(data["beacon_7"])
    beacons_label.config(text = beacons)

    room = "In Room: {:2.0f}" .format(data["room"])
    room_label.config(text = room)

    audio = "Now Playing: " + data["audio"]
    audio_label.config(text = audio)
    root.after(1000, move)
 

options= ["Device 1", 
          "Device 2",
          "Device 3",
          "Device 4",
          "Device 5", 
          "Device 6",
          "Device 7",
          "Device 8"
    ]

canEnterRoom1= [False, 
               False, 
               False,
               False, 
               False,  
               False, 
               False, 
               False, 
    ]

canEnterRoom2= [False, 
               False, 
               False,
               False, 
               False,  
               False, 
               False, 
               False, 
    ]

isActivated= [False, 
               False, 
               False,
               False, 
               False,  
               False, 
               False, 
               False, 
    ]

#pop a window up when the button "Enable a Device" is pushed

    
def selection():
    tk.messagebox.showinfo(title="Device Manager",message=clicked.get() + " has been enabled")
    # label=tk.Label(root,text=clicked.get() + " has been activated",font=16)
    # label.grid(row=5,column=1,padx=5,pady=5)

# #make buttons for the user to click when done
# buttonEnter=tk.Button(window,command=Check,text="Enter",font="16")
# buttonCancel=tk.Button(window,command=Cancel,text="Cancel",font="16")
# buttonEnter.grid(row=2,column=1,sticky="w")     #w = west
# buttonCancel.grid(row=2,column=1,sticky="e")    #e = east

label=tk.Label(mainframe,text= "Activate a Device:", font = "Arial 16 bold",fg="green").place(y=15+Offset_y, x=780+Offset_x)
#Drop Down Box

clicked=tk.StringVar(mainframe)
clicked.set(options[0])
option=tk.OptionMenu(mainframe,clicked ,*options ).place(x=970+Offset_x, y=10+Offset_y)
# option.grid(row=3,column=1)

#create boolean for checkbox
var1=tk.IntVar()
checkbox=tk.Checkbutton(mainframe,text="Room1",variable=var1).place(x=1080+Offset_x, y=15+Offset_y)
var2=tk.IntVar()
checkbox2=tk.Checkbutton(checkbox,text="Room2",variable=var2).place(x=1160+Offset_x, y=15+Offset_y)

buttonSelectDrop=tk.Button(mainframe,text="Select",command=selection).place(x=1240+Offset_x, y=8+Offset_y)
# buttonSelectDrop.grid(row=4,column=3,sticky="w")


"""" Disable a Device"""
label_dis=tk.Label(mainframe,text= "Disable a Device:", font = "Arial 16 bold" ,fg="red")
label_dis.place(x=780+Offset_x, y=55+Offset_y)


clicked_disabled=tk.StringVar(mainframe)
clicked_disabled.set(options[0])
option_dis=tk.OptionMenu(mainframe,clicked_disabled ,*options ).place(x=970+Offset_x, y=50+Offset_y)
# option.grid(row=0,column=0,padx=10,pady=10)


def selection_dis():
    # label=tk.Label(root,text=clicked.get() + " has been disabled",font=16)
    x=int(re.search(r'\d+', clicked_disabled.get()).group()) #get Device "x"
    if isActivated[x-1]==False:
        tk.messagebox.showerror(title="Device Manager",message=clicked_disabled.get() + " is not active!")
        return
    tk.messagebox.showinfo(title="Device Manager",message=clicked_disabled.get() + " has been disabled")
    canEnterRoom1[x-1]=False
    canEnterRoom2[x-1]=False
    isActivated[x-1]=False
        
buttonSelectDrop=tk.Button(mainframe,text="Select",command=selection_dis)
buttonSelectDrop.place(x=1080+Offset_x, y=48+Offset_y)
# buttonSelectDrop.grid(row=0,column=1,sticky="w")


coordinates_label= tk.Label(mainframe, text="Location (m): ",fg = "blue",
		 font = "Arial 16 bold")
coordinates_label.place(x=780+Offset_x, y=95+Offset_y)

angle_label= tk.Label(mainframe, text="Angle (degree): ",fg = "black",
		 font = "Arial 16 bold")
angle_label.place(x=1180+Offset_x, y=95+Offset_y)

beacons_label= tk.Label(mainframe, text="Distance to Beacons (m): ",fg = "Purple",
		 font = "Arial 12 bold")
beacons_label.place(x=780+Offset_x, y=135+Offset_y)

room_label= tk.Label(mainframe, text="In Room: ",fg = "Red",
		 font = "Arial 16 bold")
room_label.place(x=780+Offset_x, y=175+Offset_y)

audio_label= tk.Label(mainframe, text="Now Playing: ",fg = "Purple",
		 font = "Arial 16 bold")
audio_label.place(x=780+Offset_x, y=215+Offset_y)

# This bind window to keys so that move is called when you press a key
root.after(0, move)
 
# this creates the loop that makes the window stay 'active'
root.mainloop()