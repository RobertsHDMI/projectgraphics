from graphics import *
from lightning.CustomInputLightning import InputDialog
from lightning.BackgroundBuilder import BackgroundBuilder
from lightning.LightningBuilder import LightningBuilder

# create a 500, 400 window
win = GraphWin("Lightning", 1200, 600, autoflush=False)

# set coordinates to go from (0 , 0) in the lower left
# to (100 , 100) in the upper right .
win.setCoords(0.0, 0.0, 100, 100)

background = BackgroundBuilder(win)

lightning = LightningBuilder()

def dialog():
    while True:
        # interact with the user
        inputwin = InputDialog(2, 2, 2)
        choice = inputwin.interact()
        inputwin.close()

        if choice == "Summer":
            background.changeSeason(win,"Summer")

        if choice == "Winter":
            background.changeSeason(win,"Winter")

        if choice == "Lightning":
            lightning.drawLightning(win)

dialog()