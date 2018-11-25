from tkinter import *

root = Tk()


labal1 =Label(root,text="Name",)
labal1.grid(row =0,column=0,sticky="E")
labal2 =Label(root,text="Password")
labal2.grid(row =1,column=0,sticky="E")


entryspace =Entry(root)
entryspace.grid(row =0,column=1)
entryspace1 =Entry(root)
entryspace1.grid(row =1,column=1)

cbutton = Checkbutton(root,text ="remember password")
cbutton.grid(columnspan=2)


root.mainloop()