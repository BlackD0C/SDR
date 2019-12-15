import socket
import sys
import threading
from PIL import Image
from pygame import mixer
import webbrowser

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
        self.Button1 = tk.Button(self, width=8, height=8, text = "get file" )
        self.Button1["command"] = self.th1
        self.Button1.pack(side="left")


        self.Button3 = tk.Button(self, width=8, height=8, text = "open gps" )
        self.Button3["command"] = self.commands3
        self.Button3.pack(side="left")

        self.Button4 = tk.Button(self, width=8, height=8, text = "open music" )
        self.Button4["command"] = self.commands4
        self.Button4.pack(side="left")

        self.Button5 = tk.Button(self, width=8, height=8, text = "see movies" )
        self.Button5["command"] = self.commands5
        self.Button5.pack(side="left")

        self.Button6 = tk.Button(self, width=8, height=8, text = "open images" )
        self.Button6["command"] = self.commands6
        self.Button6.pack(side="left")

        self.Button0 = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
        self.Button0.pack(side="bottom")

#The target functions of the buttons
    def commands1(self):

#creating the socket server for creating connection , create the file after decoding the format  and save the data on the file that created
        try:
            
            s = socket.socket()
            s.bind(("localhost",9999))
            s.listen(10) # accept 10 connections at the same time

            while True:
                sc, address = s.accept()

                print("address")
                format = sc.recv(1024)
                format.decode('utf-8')
                f = filedialog.asksaveasfile(initialdir = "/",title = "Select file", mode='wb', defaultextension=format)

                while (True):       
                    l = sc.recv(1024)
                    while (l):
                            f.write(l)
                            l = sc.recv(1024)
                f.close()


                sc.close()

            s.close()
        
        except ImportError:
            print("socket problem")
        

    def commands3(self):
        # fast open a web gui with gps of google for the driver , user 
        webbrowser.open('https://www.google.co.il/maps?hl=en')
    def commands4(self):
        # open a music file / playlist of the user
        mixer.init()
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        mixer.music.load(file_path)
        mixer.music.play()

    def commands5(self):
        # fast open a web gui with movies of google for the driver , user 
        webbrowser.open('http://seret2me.blogspot.co.il/')
    def commands6(self):
        # open a picture / image
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        img = Image.open(file_path)
        img.show()

#Function that responsible for the threading of the program, the code
    def th1(self):
        t1 = threading.Thread(target=self.commands1)
        self.Button1["command"] = t1.start()

#---------------------------------------------------------------
# the  gui (tkinter) basic commands - the background and size, max size and title  
root = tk.Tk()
root.title("SDR - for your car")
root.geometry("450x350")
root.maxsize(480, 380)


background_image=tk.PhotoImage(file = "gifbglogo.gif")
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

app = Application(master=root)
#app.mainloop()

t = threading.Thread(target=app.mainloop())
t.start()
