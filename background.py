from graphics import *

window = GraphWin("Background", 1000, 700)
def  autumn():
    window.setBackground(color_rgb(255,153,50))
    img = Image(Point(500,350),"autumn.gif")
    img.draw(window)
    window.getMouse()
    window.close()
#autumn()
def winter():
    window.setBackground(color_rgb(255,255,255))
    img = Image(Point(500,350),"winter.gif")
    img.draw(window)
    window.getMouse()
    window.close()
#winter()
def spring():
    window.setBackground(color_rgb(178,255,100))
    img=Image(Point(500,350),"spring.gif")
    img.draw(window)
    window.getMouse()
    window.close()
#spring()
def summer():
    window.setBackground(color_rgb(255,255,150))
    img=Image(Point(500,350),"summer.gif")
    img.draw(window)
    window.getMouse()
    window.close()
#summer()






