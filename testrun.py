from graphics import *
from random import randrange

# create a 500, 400 window
win = GraphWin("Lightning", 1200, 600, autoflush=False)

# set coordinates to go from (0 , 0) in the lower left
# to (100 , 100) in the upper right .
win.setCoords(0.0, 0.0, 100, 100)

randX = randrange(0, 100)
randy = randrange(80, 100)
Line(Point(randX, randy), Point(randX, randy)).draw(win)

# Draw a rectangle representing the sky using a Rectangle object
sky = Rectangle(Point(0, 60), Point(100, 100))
sky.setFill("blue")
sky.draw(win)

for i in range(0, 100, 20):
    # Draw a rectangle representing the sky using a Rectangle object
    sky = Polygon(Point(0 + i, 60), Point(20 + i, 60), Point(10 + i, 40))
    sky.setFill("blue")
    sky.setOutline("blue")
    sky.draw(win)

# Draw a rectangle representing the grass using a Rectangle object
grass = Rectangle(Point(0, 0), Point(100, 20))
grass.setFill("green")
grass.draw(win)

for i in range(0, 120, 20):
    # Draw a Polygon representing the grass using a Polygon object
    grass = Polygon(Point(-20 + i, 20), Point(20 + i, 20), Point(0 + i, 60))
    grass.setFill("grey")
    grass.draw(win)

for i in range(0, 100, 30):
    if i != 60:
        # Draw a Polygon representing the grass using a Polygon object
        grass = Polygon(Point(-10 + i, 20), Point(10 + i, 20), Point(0 + i, 50))
        grass.setFill("grey")
        grass.draw(win)

# p1 = win.getMouse()
# p1.draw(win)

def drawLightning():
    p1 = win.getMouse()
    randX = randrange(0, 100)
    randY = randrange(80, 100)
    line = Line(Point(randX, randY), p1)
    line.setFill("pink")
    line.setOutline("pink")
    line.draw(win)

drawLightning()

win.mainloop()
# win.getMouse()  # Pause to view result
# win.close()
