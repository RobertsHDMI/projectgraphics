from tkinter import *
from testron2 import *

win = Tk()

win.title("My weather")
win.geometry('550x200')
tk.Label(win, text="Enter season ").grid(row=1)
box = tk.Entry(win)
box.grid(row=1, column=1)

def displaySeason():
    global box
    drawLightning(box.get())

btn = Button(win, text="Click Me", bg="blue", fg="white", command=displaySeason)
btn.grid(row=4, column=4, rowspan=3)

win.mainloop()
