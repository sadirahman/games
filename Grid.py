from tkinter import *

root = Tk()


labal1 =Label(root,text="label1")
labal2 =Label(root,text="label2")
labal3 =Label(root,text="label3")

labal1.grid(row =0,column=0)
labal2.grid(row =0,column=1)
labal3.grid(row =1,column=0)



root.mainloop()