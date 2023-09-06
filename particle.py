from math import pi
from random import randint

class Particle():
    def __init__(self, x, y, mass, speed, angle, radius):
        self.x = x
        self.y = y
        self.m = mass
        self.speed = speed
        self.angle = angle*2*pi/360
        self.r = radius
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))

