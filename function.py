from tkinter import *

root = Tk()

def printName(event):
    print("hellow i am sadi rahman ")


button1 = Button(None,text="Click me1!",fg="Blue",bg="gray")
button1.bind("<Button-1>",printName)
button1.pack()

root.mainloop()