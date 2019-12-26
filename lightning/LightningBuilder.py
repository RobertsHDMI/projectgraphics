from graphics import *
from random import randrange

class LightningBuilder:

    def __init__(self):
        randrange

    def drawLightning(self,win):
        # loop needed for animation speed (can be sped up or slowed down)
        for i in range(1000):
            # draw the starting point(random from a specific area) and the end point chosen by the user
            p1 = win.getMouse()
            randX = randrange(0, 100)
            randY = randrange(80, 100)
            line = Line(Point(randX, randY), p1)
            line.setOutline("yellow")
            line.setWidth(4)

            line_center = line.getCenter()

            line01 = Line(Point(randX + 5, randY + 5), line_center)
            line01.setOutline("yellow")
            line01.setWidth(4)

            line02 = Line(line_center, Point(p1.getX() + 5, p1.getY() + 5))
            line02.setOutline("yellow")
            line02.setWidth(4)

            def recursiveBolt(line_center):
                # draw the starting point(random from a specific area) and the end point chosen by the user
                p1 = win.getMouse()
                randX = randrange(0, 100)
                randY = randrange(80, 100)
                line = Line(Point(randX, randY), p1)
                line.setOutline("yellow")
                line.setWidth(4)

                line_center = line.getCenter()

                line01 = Line(Point(randX + 5, randY + 5), line_center)
                line01.setOutline("yellow")
                line01.setWidth(4)

                line02 = Line(line_center, Point(p1.getX() + 5, p1.getY() + 5))
                line02.setOutline("yellow")
                line02.setWidth(4)
                recursiveBolt(line_center)

            line_center01 = line01.getCenter()
            line_center02 = line02.getCenter()

            line001 = Line(Point(randX + 5, randY + 5),
                           Point(line_center01.getX() + 5, line_center01.getY() + 5))
            line001.setOutline("yellow")
            line001.setWidth(3)

            line002 = Line(Point(line_center01.getX() + 5, line_center01.getY() + 5),
                           Point(line_center.getX() + 5, line_center.getY() + 5))
            line002.setOutline("grey")
            line002.setWidth(3)

            line003 = Line(Point(line_center.getX() + 5, line_center.getY() + 5),
                           Point(line_center02.getX() + 5, line_center02.getY() + 5))
            line003.setOutline("black")
            line003.setWidth(3)

            line004 = Line(Point(line_center02.getX() + 5, line_center02.getY() + 5),
                           Point(p1.getX() + 5, p1.getY() + 5))
            line004.setOutline("pink")
            line004.setWidth(3)

            line_center001 = line001.getCenter()
            line_center002 = line002.getCenter()
            line_center003 = line003.getCenter()
            line_center004 = line004.getCenter()

            line001 = Line(Point(randX + 5, randY + 5),
                           Point(line_center001.getX() + 5, line_center001.getY() + 5))
            line001.setOutline("yellow")
            line001.setWidth(4)
            line001.draw(win)

            line002 = Line(Point(line_center001.getX() + 5, line_center001.getY() + 5),
                           Point(line_center01.getX() + 5, line_center01.getY() + 5))
            line002.setOutline("grey")
            line002.setWidth(4)
            line002.draw(win)

            line003 = Line(Point(line_center01.getX() + 5, line_center01.getY() + 5),
                           Point(line_center002.getX() + 5, line_center002.getY() + 5))
            line003.setOutline("black")
            line003.setWidth(4)
            line003.draw(win)

            line004 = Line(Point(line_center002.getX() + 5, line_center002.getY() + 5),
                           Point(line_center.getX() + 5, line_center.getY() + 5))
            line004.setOutline("pink")
            line004.setWidth(4)
            line004.draw(win)

            line005 = Line(Point(line_center.getX() + 5, line_center.getY() + 5),
                           Point(line_center003.getX() + 5, line_center003.getY() + 5))
            line005.setOutline("yellow")
            line005.setWidth(4)
            line005.draw(win)

            line006 = Line(Point(line_center003.getX() + 5, line_center003.getY() + 5),
                           Point(line_center02.getX() + 5, line_center02.getY() + 5))
            line006.setOutline("yellow")
            line006.setWidth(4)
            line006.draw(win)

            line007 = Line(Point(line_center02.getX() + 5, line_center02.getY() + 5),
                           Point(line_center004.getX() + 5, line_center004.getY() + 5))
            line007.setOutline("yellow")
            line007.setWidth(4)
            line007.draw(win)

            line008 = Line(Point(line_center004.getX() + 5, line_center004.getY() + 5),
                           Point(p1.getX() + 5, p1.getY() + 5))
            line008.setOutline("pink")
            line008.setWidth(4)
            line008.draw(win)

            line2 = Line(line_center, Point(p1.getX() + randrange(-10, 10), p1.getY() + randrange(-10, 10)))
            line2.setOutline("pink")
            line2.setWidth(3)
            line2.draw(win)

            line_center2 = line2.getCenter()

            line3 = Line(line_center2, Point(p1.getX() + randrange(-5, 5), p1.getY() + randrange(-5, 5)))
            line3.setOutline("pink")
            line3.setWidth(2)
            line3.draw(win)

            line_center3 = line3.getCenter()

            line4 = Line(line_center3, Point(p1.getX() + randrange(-5, 5), p1.getY() + randrange(-5, 5)))
            line4.setOutline("pink")
            line4.setWidth(1)
            line4.draw(win)

            # animation speed
            update(0.9)
