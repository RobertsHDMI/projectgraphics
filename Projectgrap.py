from tkinter import *

class App:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.button = Button(
            frame, text="QUIT", fg="red", command=frame.quit #frame.quit is the internal function that is
            # called to terminate the frame
        )

        self.button.pack(side=LEFT)

        self.hi_there = Button(
            frame, text="Hello", command=self.say_hi, fg="blue" #command is calling the user made function say_hi
        )

        self.hi_there.pack(side=LEFT)

    #function that prints a statement
    def say_hi(self):
        print("hi there, everyone!")

root = Tk()

app = App(root)

root.mainloop()
root.destroy()  # optional; depends on development environment
