import socket
import sys

try:
     #Python2
    import Tkinter as tk 
except ImportError:
     #Python3
    import tkinter as tk

import time
import sys
from tkinter import filedialog
#---------------------------------------------------------------
# creating the gui  (tkinter) basic commands
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
#The buttons, their target functions
    def create_widgets(self):
        self.Button1 = tk.Button(self, width=8, height=8, text = "send file" )
        self.Button1["command"] = self.commands1
        self.Button1.pack(side="left")

        self.Button2 = tk.Button(self, width=8, height=8, text = "get file" )
        self.Button2["command"] = self.commands2
        self.Button2.pack(side="left")

        self.Button0 = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
        self.Button0.pack(side="bottom")

#The target functions of the buttons
    def commands1(self):
        #print("enter home-pc ip , for localhost enter L")
        #targetip = input("")
        #targetip = "10.30.58.15"
        #targetip =  str(targetip)
        #if targetip == "L":
           # targetip = "localhost"
# creating the socket client for creating connection , then split and send the format of the file after encoding him

        s = socket.socket()
        s.settimeout(5)   # 5 seconds
        s.connect(("10.30.58.9", 9999))
        file_path = filedialog.askopenfilename()
        sf = file_path.split(".")
        for x in sf:
            if x == "jpg":
                x = "."+ x
                s.send(x.encode('utf-8'))
            if x == "mp4":
                x = "."+ x
                s.send(x.encode('utf-8'))
            if x == "png":
                x = "."+ x
                s.send(x).encode('utf-8')
        f = open(file_path, "rb")
        l = f.read(1024)
        while (l):
            s.send(l)
            l = f.read(1024)
        s.close()


    def commands2(self):
        print("not now")
#---------------------------------------------------------------
# the  gui (tkinter) basic commands - the background and size, max size and title  
root = tk.Tk()
root.title("SDR -for Home pc")
root.geometry("1080x720")
root.maxsize(1820, 1280)

background_image=tk.PhotoImage(file = "gifbglogo.gif")
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

app = Application(master=root)
app.mainloop()
