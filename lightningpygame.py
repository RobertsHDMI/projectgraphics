from math import *
from pygame import *
from random import *

#---------------------------------------------------------------------

def lightning(screen, x, y, size, ang, count):
    if size > 5:
        rang = radians(ang)
        x2 = x-size*cos(rang)
        y2 = y+size*sin(rang)
        draw.line(screen,(200,180,0), (x,y),(x2,y2))
        count = lightning(screen,x2,y2,size-randint(1,10),ang-randint(-20,10), count)
        count = lightning(screen,x2,y2,size-randint(1,10),ang+randint(-10,30), count)
    return count

#---------------------------------------------------------------------

screen = display.set_mode((800,600))

print (lightning(screen, 400, 0, 50, randint(60,100), 0))
display.flip()

time.wait(5000)

quit()
