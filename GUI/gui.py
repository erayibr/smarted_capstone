import tkinter as tk
#from tkinter import *
import os
import json
 
# Create the window with the Tk class
root = tk.Tk()
root.state('zoomed')
root.title("SMARTED Visitor Tracking Software")
# Create the canvas and make it visible with pack()
# canvas = tk.Canvas(root, width=1920, height=1080, highlightthickness=0, relief='ridge')
canvas = tk.Canvas(root, width=1024, height=720, bg="grey")
canvas.pack() # this makes it visible

map = tk.PhotoImage(file="map.png")
canvas.create_image(0, 0, anchor=tk.NW, image=map)

# Loads and create image (put the image in the folder)
img = tk.PhotoImage(file="visitor1.png")
y = 0
x = 0
image = canvas.create_image(x + 53, y + 621, image=img)



#pop a window up when the button "Enable a Device" is pushed
def EnableDevice():
    
    window =tk.Tk()
    window.title("Enter new visitor info")
    window.geometry("600x300")
    #window.protocol ('WM_DELETE_WINDOW', (lambda: 'pass') ())
    
          
    L1=tk.Label(window,text="Username:",font=16)
    L2=tk.Label(window,text="Password:",font=16)
    L1.grid(row=0,column=0,padx=5,pady=5)
    L2.grid(row=1,column=0,padx=5,pady=5)
    
        
    username=tk.StringVar(window)  
    password=tk.StringVar(window)
    
    # get entry from user
    t1= tk.Entry(window,textvariable=username,font=16,width=30)
    t2= tk.Entry(window,textvariable=password,font=16,show="*",width=30)
    t1.grid(row=0,column=1)
    t2.grid(row=1,column=1)
    
    #event handler for "Enter" button
    def Check():
        if username.get()=="admin" and password.get()=="smarted":
            tk.messagebox.showinfo(title="New Visitor",message="New visitor added successfully")
        else:
            tk.messagebox.showerror(title="Data Error",message="Invalid visitor data!")
    
    #event handler for "Cancel" button
    def Cancel():
        status=tk.messagebox.askyesno(title="Exit?",message="Do you want to cancel ?" +" Any unsaved entry will be lost")
        if status==True:
            window.destroy()  #deallocate all objects tied to "window"
        else:
            tk.messagebox.showwarning(title="Cancelled",message="Please enter new visitor data")
            
    def selection():
        tk.messagebox.showinfo(title="Device Manager",message=clicked.get() + " has been enabled")
        label=tk.Label(window,text=clicked.get() + " has been activated",font=16)
        label.grid(row=5,column=1,padx=5,pady=5)
    
    #make buttons for the user to click when done
    buttonEnter=tk.Button(window,command=Check,text="Enter",font="16")
    buttonCancel=tk.Button(window,command=Cancel,text="Cancel",font="16")
    buttonEnter.grid(row=2,column=1,sticky="w")     #w = west
    buttonCancel.grid(row=2,column=1,sticky="e")    #e = east
    
    
    #Drop Down Box
    options= ["Device 1", 
              "Device 2",
              "Device 3",
              "Device 4",
              "Device 5", 
              "Device 6",
              "Device 7",
              "Device 8"
        ]
    clicked=tk.StringVar(window)
    clicked.set(options[0])
    option=tk.OptionMenu(window,clicked ,*options )
    option.grid(row=3,column=1)
    
    
    buttonSelectDrop=tk.Button(window,text="Select",command=selection)
    buttonSelectDrop.grid(row=4,column=3,sticky="w")

    #  # #to prevent opening multiple child windows 
    # window.transient()
    # window.focus()
    # window.grab_set()
    # root.wait_window(window)
   
    window.mainloop()

def DisableDevice():
    window =tk.Tk()
    window.title("Enter new visitor info")
    window.geometry("400x150")
    
    #Drop Down Box
    options= ["Device 1", 
              "Device 2",
              "Device 3",
              "Device 4",
              "Device 5", 
              "Device 6",
              "Device 7",
              "Device 8"
        ]
    clicked=tk.StringVar(window)
    clicked.set(options[0])
    option=tk.OptionMenu(window,clicked ,*options )
    option.grid(row=0,column=0,padx=10,pady=10)
    
    
    def selection():
        label=tk.Label(window,text=clicked.get() + " has been disabled",font=16)
        tk.messagebox.showinfo(title="Device Manager",message=clicked.get() + " has been disabled")
        label.grid(row=1,column=1,padx=5,pady=5)
    
    buttonSelectDrop=tk.Button(window,text="Select",command=selection)
    buttonSelectDrop.grid(row=0,column=1,sticky="w")

   
    window.mainloop()


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

newVisitor= tk.Button(root,text="Enable a Device", padx=10, pady=5, fg="white",
                      bg="#204D40",command=EnableDevice)

newVisitor.pack()


disableVisitor= tk.Button(root,text="Disable a Device", padx=10, pady=5, fg="white",
                      bg="#204D40" ,command=DisableDevice )

disableVisitor.pack()

 
# This bind window to keys so that move is called when you press a key
root.after(1000, move)

 
# this creates the loop that makes the window stay 'active'
root.mainloop()