from tkinter import *

root = Tk()


topframe = Frame(root)

topframe.pack()

botframe =Frame(root)

botframe.pack(side=BOTTOM)


button1 = Button(None,text="Click me1!",fg="Blue",bg="gray")
button1.pack()
button2 = Button(None,text="Click me2!",fg="red",bg="black")
button2.pack(fill=X)
button3 = Button(None,text="hello1!",fg="black" ,bg="yellow")
button3.pack(side=RIGHT,fill=Y)
button4 = Button(None,text="hello2!",fg="green")
button4.pack()
root.mainloop()