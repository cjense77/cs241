import arcade
from point import Point
from velocity import Velocity

class FlyingObject():
    def __init__(self, x = 0, y = 0, dx = 0, dy = 0):
        self.center = Point(x, y)
        self.velocity = Velocity(dx, dy)

    def advance(self):
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy
