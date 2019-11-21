from graphics import *
from random import randrange

# create a 500, 400 window
win = GraphWin("Lightning", 800, 500)

# set coordinates to go from (0 , 0) in the lower left
# to (100 , 100) in the upper right .
win.setCoords(0.0, 0.0, 100, 100)

randX = randrange(0, 100)
randy = randrange(80, 100)
Line(Point(randX, randy), Point(randX, randy)).draw(win)

# Draw a rectangle representing the sky using a Rectangle object
sky = Rectangle(Point(0, 80), Point(100, 100))
sky.setFill("blue")
sky.draw(win)

#p1 = win.getMouse()
#p1.draw(win)
p2 = win.getMouse()
p2.draw(win)

randX = randrange(0, 100)
randY = randrange(80, 100)
line = Line(Point(randX, randY), p2)
line.setFill("black")
line.setOutline("black")
line.draw(win)

win.getMouse()  # Pause to view result
win.close()
