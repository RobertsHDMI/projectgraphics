from graphics import *
from random import randrange
from math import sin, cos, radians

class Projectile:
    """Simulates the flight of simple projectiles near the earth's
    surface , ignoring wind resistance . Tracking is done in two
    dimensions , height (y) and distance (x) . """

    def __init__(self, angle, velocity, height, width):
        """Create a projectile with given launch angle , initial
        velocity and height . """
        self.xpos = width
        self.ypos = height
        theta = radians(angle)
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)

    def update(self, time):
        """Update the state of this projectile to move it time seconds farther into its flight"""
        self.xpos = self.xpos + time * self.xvel
        self.ypos = self.ypos + time * self.yvel

    def getY(self):
        "Returns the y position (height) of this projectile ."
        return self.ypos

    def getX(self):
        "Returns the x position (distance) of this projectile ."
        return self.xpos

class BoltDraw:
    """Simulates the flight of simple projectiles near the earth's
    surface , ignoring wind resistance . Tracking is done in two
    dimensions , height (y) and distance (x) . """

    def __init__(self, startingPoint, endingPoint):
        """Create a projectile with given launch angle , initial
        velocity and height . """


class ShotTracker:
    def __init__(self, win, angle, velocity, height, width):
        """win is the GraphWin to display the shot . angle, velocity,
            and height are initial projectile parameters .
        """
        self.proj = Projectile(angle, velocity, height, width)

        self.marker = Circle(Point(0, height), 3)
        self.marker.setFill("red")
        self.marker.setOutline("red")
        #self.marker.draw(win)

    def update(self, dt):
        """Move the shot dt seconds farther along its flight"""

        # update the projectile
        self.proj.update(dt)

        # move the circle to the new projectile location
        center = self.marker.getCenter()
        dx = self.proj.getX() - center.getX()
        dy = self.proj.getY() - center.getY()
        self.marker.move(dx + randrange(0,5), dy + randrange(0,5))

        point1 = Point(dx + randrange(0,5),dy + randrange(0,5))
        point2 = Point(dx,dy)

        # draw the starting point(random from a specific area) and the end point chosen by the user
        line = Line(point1, point2)
        line.setFill("white")
        line.setOutline("blue")
        line.setWidth(3)
        line.draw(win)

    def getX(self):
        """return the current x coordinate of the shot's center"""
        return self.proj.getX()

    def getY(self):
        """return the current y coordinate of the shot's center"""
        return self.proj.getY()

    def undraw(self):
        """undraw the shot"""
        self.marker.undraw()


# create a 500, 400 window
win = GraphWin("Lightning", 1200, 600, autoflush=False)

# set coordinates to go from (0 , 0) in the lower left
# to (100 , 100) in the upper right .
win.setCoords(0.0, 0.0, 100, 100)

# the angle should be random but always point down - need to find the interval of the angle
shot = ShotTracker(win, randrange(180,360), 1, 50, 50)

while 0 <= shot.getY() <= 100 and 0 < shot.getX() <= 100:
    shot.update(1/1)
    update(50)

win.mainloop()