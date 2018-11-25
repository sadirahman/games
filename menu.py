from tkinter import *

root = Tk()
def random():
    print("this is a statement")
mainmenu =Menu(root)

root.configure(menu=mainmenu)
submenu=Menu(mainmenu)
mainmenu.add_cascade(label="file",menu=submenu)
mainmenu.add_cascade(label="help",menu=submenu)
submenu.add_command(label="random func",command=random)
submenu.add_command(label="random file",command=random)

submenu.add_separator()
submenu.add_command(label="new",command=random)




root.mainloop()