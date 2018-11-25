from tkinter import *

root = Tk()

def leftClick(event):
    print("left ")

def rightClick(event):
    print("right ")

def scroll(event):
    print("Scroll ")

def leftkey(event):
    print("left key prassed ")

def rightkey(event):
    print("right key prassed ")

root.geometry("500x500")

root.bind("<Button-1>",leftClick)
root.bind("<Button-2>",rightClick)
root.bind("<Button-3>",scroll)
root.bind("<Left>",leftkey)
root.bind("<Right>",rightkey)

root.mainloop()