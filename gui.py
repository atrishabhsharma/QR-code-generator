from tkinter import * 

import tkinter as tk

import tkinter.messagebox

from QRcode import QR_print



class QRCODE(): 

  

    def __init__(self,master):

       self.label= Label(master,text="Enter data").pack()
       
       self.entry= Entry(master,textvariable=ab,bg="pink",fg="black").pack() #textvariable is to store entered data

       self.button= Button(master,text="Print",command=self.printQR).pack()

    def printQR(self):
        text=ab.get() #value store
        from tkinter import * 

import tkinter as tk

import tkinter.messagebox

from QRcode import QR_print



class QRCODE(): 

  

    def __init__(self,master):

       self.label= Label(master,text="Enter data").pack()
       
       self.entry= Entry(master,textvariable=ab,bg="pink",fg="black").pack() #textvariable is to store entered data

       self.button= Button(master,text="Print",command=self.printQR).pack()

    def printQR(self):
        text=ab.get() #value store
        #### status bar ####
        status = Label(root,text="processing....",bd=1,relief=SUNKEN,anchor=W)
        status.pack(side=BOTTOM,fill=X)
        tkinter.messagebox.showinfo("GENERATED"," your QR-code is generated")       
        QR_print(text)
            
    
   
        



root=tk.Tk() # main pop-up window

ab=tk.StringVar() #textvariable type

root.title("QR-CODE generator")

root.geometry("200x200")

b=QRCODE(root)

# above all this will run
root.mainloop()
        QR_print(text)


root=tk.Tk() # main pop-up window

ab=tk.StringVar() #textvariable type

root.title("QR-CODE generator")

root.geometry("200x200")

b=QRCODE(root)

# above all this will run
root.mainloop()
