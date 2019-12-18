from graphics import *
from playsound import playsound
from enum import Enum
import threading

class Season(Enum):
    SUMMER = 1
    WINTER = 2
    AUTUMN = 3
    SPRING = 4

window = GraphWin("Background", 1000, 700)

def setSeason(weatherAsString):
    backgroundColor = color_rgb(255, 153, 50)
    imageName = ""
    soundName = ""

    if weatherAsString == "autumn":
        backgroundColor = color_rgb(255, 153, 50)
        imageName = "autumn.gif"
        soundName = "autumn.mp3"

    elif weatherAsString == "winter":
        backgroundColor = color_rgb(255, 255, 255)
        imageName = "winter.gif"
        soundName = "winter.mp3"

    elif weatherAsString == "spring":
        backgroundColor = color_rgb(178, 255, 100)
        imageName = "spring.gif"
        soundName = "birds.mp3"

    elif weatherAsString == "summer":
        backgroundColor = color_rgb(255, 255, 150)
        imageName = "summer.gif"
        soundName = "summer.mp3"

    window.setBackground(backgroundColor)
    img = Image(Point(500, 350), imageName)
    img.draw(window)
    soundThread = threading.Thread(target=playsound, args=(soundName,))
    soundThread.start()
    window.getMouse()
    window.close()

def changeSeason(weather :Season ):
    backgroundColor = color_rgb(255, 153, 50)
    imageName = ""
    soundName = ""

    if weather == Season.AUTUMN:
        backgroundColor = color_rgb(255, 153, 50)
        imageName = "autumn.gif"
        soundName = "autumn.mp3"

    elif weather == Season.WINTER:
        backgroundColor = color_rgb(255, 255, 255)
        imageName = "winter.gif"
        soundName = "winter.mp3"

    elif weather == Season.SPRING:
        backgroundColor = color_rgb(178, 255, 100)
        imageName = "spring.gif"
        soundName = "birds.mp3"

    elif weather == Season.SUMMER:
        backgroundColor = color_rgb(255, 255, 150)
        imageName = "summer.gif"
        soundName = "summer.mp3"

    window.setBackground(backgroundColor)
    img = Image(Point(500, 350), imageName)
    img.draw(window)
    print(weather.value)
    soundThread = threading.Thread(target=playsound, args=(soundName,))
    soundThread.start()
    window.getMouse()
    window.close()







