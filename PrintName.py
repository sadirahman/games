from tkinter import *

root = Tk()

def printName():
    print("hellow i am sadi rahman ")


button1 = Button(None,text="Click me1!",fg="Blue",bg="gray",command=printName)
button1.pack()

root.mainloop()