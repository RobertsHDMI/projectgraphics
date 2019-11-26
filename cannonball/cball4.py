# cball4.py
from cannonball.projectile import Projectile


def getInputs():
    a = float(input("Enter the launch angle (in degrees): "))
    v = float(input("Enter the initial velocity( in meters/sec): "))
    h = float(input("Enter the initial height( in meters): "))
    t = float(input("Enter the time interval between position calculations: "))
    return a, v, h, t


def main():
    angle, vel, hO, time = getInputs()
    cball = Projectile(angle, vel, hO)
    while cball.getY() >= 0:
        cball.update(time)
    print("\nDistance traveled: {0:0.1f} meters.".format(cball.getX()))


main()
