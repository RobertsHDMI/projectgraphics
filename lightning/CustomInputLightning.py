from graphics import *
from lightning.ButtonLightning import Button

class InputDialog:
    """A custom window for getting simulation values (angle, velocity,
    and height) from the user."""

    def __init__(self, angle, vel, height):
        """Build and display the input window"""
        self.win = win = GraphWin("Initial Values", 200, 300)
        win.setCoords(0, 0, 10, 10)

        self.summer = Button(win, Point(2, 2), 4, 2, "Summer")
        self.summer.activate()
        self.winter = Button(win, Point(2, 4), 4, 2, "Winter")
        self.winter.activate()
        self.lightning = Button(win, Point(2, 6), 4, 2, "Lightning")
        self.lightning.activate()

    def interact(self):
        """ wait for user to click Quit or Fire button
        Returns a string indicating which button was clicked"""
        while True:
            pt = self.win.getMouse()
            if self.summer.clicked(pt):
                return "Summer"
            if self.winter.clicked(pt):
                return "Winter"
            if self.lightning.clicked(pt):
                return "Lightning"

    def close(self):
        """close the input window"""
        self.win.close()
