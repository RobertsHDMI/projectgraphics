from tkinter import *
from background import *

window=Tk()

window.title("My weather")
window.geometry('550x200')
tk.Label(window, text="Enter season ").grid(row=1)
box = tk.Entry(window)
box.grid(row=1, column=1)

def displaySeason():
    global box
    setSeason(box.get())

btn = Button(window, text="Click Me", bg="blue", fg="white", command=displaySeason)
btn.grid(row=4, column=4, rowspan=3)

window.mainloop()