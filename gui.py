from tkinter import * 

import tkinter as tk

from QRcode import QR_print



class QRCODE(): 

  

    def __init__(self,master):

       self.label= Label(master,text="Enter data").pack()
       
       self.entry= Entry(master,textvariable=ab,bg="pink",fg="black").pack() #textvariable is to store entered data

       self.button= Button(master,text="Print",command=self.printQR).pack()

    def printQR(self):
        text=ab.get() #value store
      
        QR_print(text)


root=tk.Tk() # main pop-up window

ab=tk.StringVar() #textvariable type

root.title("QR-CODE generator")

root.geometry("200x200")

b=QRCODE(root)

# above all this will run
root.mainloop()
