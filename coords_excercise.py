from graphics import *

# create a default 200x200 window
win = GraphWin("Tic-Tac-Toe ", 500, 400)

# set coordinates to go from (0 , 0) in the lower left
# to (3 , 3) in the upper right .
win.setCoords(0.0, 0.0, 5, 7)

# Draw vertical lines
Line(Point(0, 7), Point(0, 4)).draw(win)
Line(Point(1, 7), Point(1, 4)).draw(win)
Line(Point(2, 7), Point(2, 4)).draw(win)
Line(Point(3, 7), Point(3, 4)).draw(win)

# Draw horizontal lines
Line(Point(0, 7), Point(3, 7)).draw(win)
Line(Point(0, 6), Point(3, 6)).draw(win)
Line(Point(0, 5), Point(3, 5)).draw(win)
Line(Point(0, 4), Point(3, 4)).draw(win)

# Draw an oval
oval = Oval(Point(3.2, 4), Point(4.7, 6.4))
oval.draw(win)

# Draw a rectangle using a Rectangle object
rect = Rectangle(Point(0.2, 0.2), Point(2.8, 3.5))
rect.draw(win)

# Draw a triangle using Line objects
Line(Point(3, 0.4), Point(4, 3.5)).draw(win)
Line(Point(4, 3.5), Point(4.8, 1.2)).draw(win)
Line(Point(4.8, 1.2), Point(3, 0.4)).draw(win)

# Draw triangle using Polygon object
p1 = Point(3.1, 0.5)
p2 = Point(4, 3.3)
p3 = Point(4.7, 1.2)
triangle = Polygon(p1, p2, p3)
triangle.setFill("peachpuff")
triangle.setOutline("cyan")
triangle.draw(win)

win.getMouse()  # Pause to view result
win.close()
