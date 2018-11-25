from tkinter import *
import tkinter.messagebox
root = Tk()

tkinter.messagebox.showinfo("Did you know that tha world" )

answer =tkinter.messagebox.askquestion(("Question 1","Are you human ?"))

if answer == "yes":
    tkinter.messagebox.showinfo("Congrate!")
if answer =="no":
    tkinter.messagebox.showinfo("alien")



root.mainloop()