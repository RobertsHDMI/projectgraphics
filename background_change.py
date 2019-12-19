from graphics import *
from die_cast.button import Button

# create a 500, 400 window
win = GraphWin("Lightning", 1200, 600, autoflush=False)

# set coordinates to go from (0 , 0) in the lower left
# to (100 , 100) in the upper right .
win.setCoords(0.0, 0.0, 100, 100)

spring = Button(win, Point(95, 95), 5, 5, "Spring")
spring.activate()
quit = Button(win, Point(95, 85), 5, 5, "Quit")
quit.activate()



""" wait for user to click Quit or Fire button Returns a string indicating which button was clicked"""
while True:
    pt = win.getMouse()
    if spring.clicked(pt):
        image = Image.open("D://Engagement2/backgrounds/500x400.png")
        backgroundImage = ImageTk.PhotoImage(image)
        spring = Image(Point(50, 50), "img/spring.gif")
        Image.draw(spring, win)
    if quit.clicked(pt):
        win.close()

