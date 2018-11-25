from tkinter import *

root = Tk()

canvas = Canvas(root,width=300,height=300)
canvas.pack()

canvas.create_rectangle(20,20,100,270)
canvas.create_line(0,0,300,300)

root.mainloop()