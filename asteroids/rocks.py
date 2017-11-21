from flying_object import FlyingObject
from point import Point
from velocity import Velocity
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
    def __init__(self, center=Point(), velocity=Velocity(), radius=10, angle=0):
        super().__init__(center=center, velocity=velocity, radius=radius, angle=angle)
        self.spin = 0

    @abstractmethod
    def break_apart(self):
        pass

    @abstractmethod
    def draw(self):
        pass


class BigRock(Rock):
    def __init__(self, screen_width, screen_height):
        super().__init__(center=Point(x=random.uniform(0, screen_width),
                                      y=random.uniform(0, screen_height)),
                         velocity=Velocity(dx=math.cos(random.uniform(0,2*math.pi))*BIG_ROCK_SPEED,
                                           dy=math.sin(random.uniform(0,2*math.pi))*BIG_ROCK_SPEED,
                                           da=BIG_ROCK_SPIN),
                         radius=BIG_ROCK_RADIUS)

    def break_apart(self):
        debris1 = MediumRock(Point(self.center.x, self.center.y),
                             Velocity(self.velocity.dx, self.velocity .dy + 2, MEDIUM_ROCK_SPIN))
        debris2 = MediumRock(Point(self.center.x, self.center.y),
                             Velocity(self.velocity.dx, self.velocity .dy - 2, MEDIUM_ROCK_SPIN))
        debris3 = SmallRock(Point(self.center.x, self.center.y),
                            Velocity(self.velocity.dx + 5, self.velocity .dy, SMALL_ROCK_SPIN))
        self.kill()

        return [debris1, debris2, debris3]


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
    def __init__(self, center, velocity):
        super().__init__(center=center,
                         velocity=velocity,
                         radius=MEDIUM_ROCK_RADIUS)

    def break_apart(self):
        debris1 = SmallRock(Point(self.center.x, self.center.y),
                            Velocity(self.velocity.dx + 1.5, self.velocity .dy + 1.5, SMALL_ROCK_SPIN))
        debris2 = SmallRock(Point(self.center.x, self.center.y),
                            Velocity(self.velocity.dx - 1.5, self.velocity .dy - 1.5, SMALL_ROCK_SPIN))

        self.kill()

        return [debris1, debris2]

    def draw(self):
        img = 'images/meteorGrey_med1.png'
        texture = arcade.load_texture(img)

        width = texture.width
        height = texture.height

        arcade.draw_texture_rectangle(self.center.x,
                                      self.center.y,
                                      width,
                                      height,
                                      texture,
                                      self.angle)


class SmallRock(Rock):
    def __init__(self, center, velocity):
        super().__init__(center=center,
                         velocity=velocity,
                         radius=SMALL_ROCK_RADIUS)

    def break_apart(self):
        self.kill()
        return []

    def draw(self):
        img = 'images/meteorGrey_small1.png'
        texture = arcade.load_texture(img)

        width = texture.width
        height = texture.height

        arcade.draw_texture_rectangle(self.center.x,
                                      self.center.y,
                                      width,
                                      height,
                                      texture,
                                      self.angle)
