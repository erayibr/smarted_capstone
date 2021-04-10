import tkinter as tk
#from tkinter import *
import os
import json
import re
 
# Create the window with the Tk class
root = tk.Tk()
root.state('zoomed')
root.title("SMARTED Visitor Tracking Software")
#to manage the left of the screen
leftframe=tk.Frame(root).pack(side="left")
#to manage the right of the screen
rightframe=tk.Frame(leftframe).pack(side="right")
# Create the canvas and make it visible with pack()
# canvas = tk.Canvas(root, width=1920, height=1080, highlightthickness=0, relief='ridge')
canvas = tk.Canvas(leftframe, width=1024, height=720, bg="white")
canvas.pack(side="left") # this makes it visible

map = tk.PhotoImage(file="map.png")
canvas.create_image(0, 0, anchor=tk.NW, image=map)

# Loads and create image (put the image in the folder)
img = tk.PhotoImage(file="visitor1.png")
y = 0
x = 0
image = canvas.create_image(x + 53, y + 621, image=img)

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



label=tk.Label(rightframe,text= "Activate a Device:",font=20,fg="green").pack()
#Drop Down Box

clicked=tk.StringVar(rightframe)
clicked.set(options[0])
option=tk.OptionMenu(rightframe,clicked ,*options ).pack()
# option.grid(row=3,column=1)




#create boolean for checkbox
var1=tk.IntVar()
checkbox=tk.Checkbutton(rightframe,text="Room1",variable=var1).pack()
var2=tk.IntVar()
checkbox2=tk.Checkbutton(checkbox,text="Room2",variable=var2).pack()

buttonSelectDrop=tk.Button(rightframe,text="Select",command=selection).pack()
# buttonSelectDrop.grid(row=4,column=3,sticky="w")


"""" Disable a Device"""
label_dis=tk.Label(rightframe,text= "Disable a Device:",font=20,fg="red")
label_dis.pack()


clicked_disabled=tk.StringVar(rightframe)
clicked_disabled.set(options[0])
option_dis=tk.OptionMenu(rightframe,clicked_disabled ,*options ).pack()
# option.grid(row=0,column=0,padx=10,pady=10)


def selection_dis():
    # label=tk.Label(root,text=clicked.get() + " has been disabled",font=16)
    x=int(re.search(r'\d+', clicked_disabled.get()).group()) #get Device "x"
    if isActivated[x-1]==False:
        tk.messagebox.showerror(title="Device Manager",message=clicked_disabled.get() + " has already been disabled!")
        return
    tk.messagebox.showinfo(title="Device Manager",message=clicked_disabled.get() + " has been disabled")
    canEnterRoom1[x-1]=False
    canEnterRoom2[x-1]=False
    isActivated[x-1]=False
        
        
        
        
    

buttonSelectDrop=tk.Button(rightframe,text="Select",command=selection_dis)
buttonSelectDrop.pack()
# buttonSelectDrop.grid(row=0,column=1,sticky="w")

   
    # window.mainloop()


def move(event = "none"):
    global x, y
    with open((os.path.dirname(os.getcwd()) + '/Server/coordinates.txt'), 'r') as file:
        data = json.loads(file.read( ))
    canvas.move(image, (data["x"] - x)*160, (y - data["y"])*160)
    x = data["x"]
    y = data["y"]
    root.after(1000, move)
    
# # get entry from user
# enter= tk.Entry(root,width=30, bg="green",fg="white",borderwidth= 10)
# enter.pack()

# newVisitor= tk.Button(root,text="Enable a Device", padx=10, pady=5, fg="white",
#                       bg="#204D40",command=EnableDevice)

# newVisitor.pack()


# disableVisitor= tk.Button(root,text="Disable a Device", padx=10, pady=5, fg="white",
#                       bg="#204D40" ,command=DisableDevice )

# disableVisitor.pack()

 
# This bind window to keys so that move is called when you press a key
root.after(1000, move)


# this creates the loop that makes the window stay 'active'
root.mainloop()