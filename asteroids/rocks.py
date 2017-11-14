from flying_object import FlyingObject
from abc import abstractmethod
import arcade
import random
import math

BIG_ROCK_SPIN = 1
BIG_ROCK_SPEED = 1.5
BIG_ROCK_RADIUS = 15

MEDIUM_ROCK_SPIN = -2
MEDIUM_ROCK_RADIUS = 5

SMALL_ROCK_SPIN = 5
SMALL_ROCK_RADIUS = 2


class Rock(FlyingObject):
    def __init__(self, x=0, y=0, dx=1, dy=1, da=0, radius=10, angle=0):
        super().__init__(x=x, y=y, dx=dx, dy=dy, da=da, radius=radius, angle=angle)
        self.spin = 0

    @abstractmethod
    def hit(self):
        pass

    @abstractmethod
    def draw(self):
        pass


class BigRock(Rock):
    def __init__(self, screen_width, screen_height):
        super().__init__(x=random.uniform(0, screen_width),
                         y=random.uniform(0, screen_height),
                         dx=math.cos(random.uniform(0,2*math.pi))*BIG_ROCK_SPEED,
                         dy=math.sin(random.uniform(0,2*math.pi))*BIG_ROCK_SPEED,
                         da=BIG_ROCK_SPIN,
                         radius=BIG_ROCK_RADIUS)

    def hit(self):
        pass

    def draw(self):
        img = 'images/meteorGrey_big1.png'
        texture = arcade.load_texture(img)

        width = texture.width
        height = texture.height

        arcade.draw_texture_rectangle(self.center.x,
                                      self.center.y,
                                      width,
                                      height,
                                      texture,
                                      self.angle)


class MediumRock(Rock):
    def __init__(self):
        super().__init__()

    def hit(self):
        pass

    def draw(self):
        pass


class SmallRock(Rock):
    def __init__(self):
        super().__init__()

    def hit(self):
        pass

    def draw(self):
        pass
