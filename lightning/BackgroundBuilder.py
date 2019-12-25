from graphics import *

class BackgroundBuilder:
    """Class containing methods for drawing the background as a parameter the string
    containing the seasons chosen by the user
    """

    def __init__(self, win):
        self.season = "Summer"
        if self.season == "Summer":
            # Draw a rectangle representing the sky using a Rectangle object
            sky = Rectangle(Point(0, 60), Point(100, 100))
            sky.setFill("blue")
            sky.draw(win)

            sun = Circle(Point(80, 80), 10)
            sun.setFill("yellow")
            sun.draw(win)

            for i in range(0, 100, 20):
                # Draw a series of polygons representing the sky using a Rectangle object, in order to fill up the space
                # between mountains with sky
                sky = Polygon(Point(0 + i, 60), Point(20 + i, 60), Point(10 + i, 40))
                sky.setFill("blue")
                sky.setOutline("blue")
                sky.draw(win)

            # Draw a rectangle representing the grass using a Rectangle object
            grass = Rectangle(Point(0, 0), Point(100, 20))
            grass.setFill("green")
            grass.draw(win)

            for i in range(0, 120, 20):
                # Draw a series of Polygons representing the mountains using a Polygon object
                mountains = Polygon(Point(-20 + i, 20), Point(20 + i, 20), Point(0 + i, 60))
                mountains.setFill("grey")
                mountains.draw(win)

            for i in range(0, 100, 30):
                if i != 60:
                    # Draw a Polygon representing the mountains using a Polygon object
                    mountains = Polygon(Point(-10 + i, 20), Point(10 + i, 20), Point(0 + i, 50))
                    mountains.setFill("grey")
                    mountains.draw(win)

        if self.season == "Winter":
            # Draw a rectangle representing the sky using a Rectangle object
            sky = Rectangle(Point(0, 60), Point(100, 100))
            sky.setFill("blue")
            sky.draw(win)

            for i in range(0, 100, 20):
                # Draw a series of polygons representing the sky using a Rectangle object, in order to fill up the space
                # between mountains with sky
                sky = Polygon(Point(0 + i, 60), Point(20 + i, 60), Point(10 + i, 40))
                sky.setFill("blue")
                sky.setOutline("blue")
                sky.draw(win)

            # Draw a rectangle representing the grass using a Rectangle object
            grass = Rectangle(Point(0, 0), Point(100, 20))
            grass.setFill("green")
            grass.draw(win)

            for i in range(0, 120, 20):
                # Draw a series of Polygons representing the mountains using a Polygon object
                mountains = Polygon(Point(-20 + i, 20), Point(20 + i, 20), Point(0 + i, 60))
                mountains.setFill("grey")
                mountains.draw(win)

            for i in range(0, 120, 20):
                # Draw a series of Polygons representing the snow on mountains using a Polygon object
                snow = Polygon(Point(-5 + i, 50), Point(5 + i, 50), Point(0 + i, 60))
                snow.setFill("white")
                snow.draw(win)

            for i in range(0, 100, 30):
                if i != 60:
                    # Draw a Polygon representing the mountains using a Polygon object
                    mountains = Polygon(Point(-10 + i, 20), Point(10 + i, 20), Point(0 + i, 50))
                    mountains.setFill("grey")
                    mountains.draw(win)

            for i in range(0, 100, 30):
                if i != 60:
                    # Draw a series of Polygons representing the snow on mountains using a Polygon object
                    snow = Polygon(Point(-3.5 + i, 40), Point(3.5 + i, 40), Point(0 + i, 50))
                    snow.setFill("white")
                    snow.draw(win)

    def changeSeason(self, seasonParameter):
        self.season = "Winter"