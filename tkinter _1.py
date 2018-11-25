from tkinter import *

root = Tk()


labal1 =Label(root,text="label1")
labal2 =Label(root,text="label2")
labal3 =Label(root,text="label3")

labal1.grid(row =0,column=0)
labal2.grid(row =0,column=1)
labal3.grid(row =1,column=0)


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