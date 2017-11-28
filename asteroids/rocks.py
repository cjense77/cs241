"""
File: rocks.py
Author: Colin Jensen
Contains classes for various sizes of flying rocks in an arcade game
"""

from flying_object import FlyingObject
from point import Point
from velocity import Velocity
from abc import abstractmethod
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
    """
    An abstract base class for a flying rock in an arcade game
    """
    def __init__(self, center=Point(), velocity=Velocity(), radius=10, angle=0):
        """
        Initialize a flying rock
        :param center:
        :param velocity:
        :param radius:
        :param angle:
        """
        super().__init__(center=center, velocity=velocity, radius=radius, angle=angle)
        self.spin = 0

    def draw(self, image):
        super().draw(image)

    @abstractmethod
    def break_apart(self):
        pass


class BigRock(Rock):
    """
    A big flying Rock object
    """
    def __init__(self, screen_width, screen_height):
        """
        Initialize a BigRock
        :param screen_width: int
        :param screen_height: int
        """

        # Define acceptable range for big rocks to start (far enough away from the ship that
        # the ship is not instantly killed)
        acceptable_start_x = [x for x in range(screen_width) if not screen_width/3 < x < 2*screen_width/3]
        acceptable_start_y = [y for y in range(screen_height) if not screen_height/3 < y < 2*screen_height/3]
        super().__init__(center=Point(x=random.choice(acceptable_start_x),
                                      y=random.choice(acceptable_start_y)),
                         velocity=Velocity(dx=math.cos(random.uniform(0, 2*math.pi))*BIG_ROCK_SPEED,
                                           dy=math.sin(random.uniform(0, 2*math.pi))*BIG_ROCK_SPEED,
                                           da=BIG_ROCK_SPIN),
                         radius=BIG_ROCK_RADIUS)

    def draw(self):
        """
        Draw a BigRock on the screen
        :return:
        """
        super().draw('images/meteorGrey_big1.png')

    def break_apart(self):
        """
        Define what happens when something collides with a BigRock
        :return: a list of smaller Rock objects
        """
        debris1 = MediumRock(Point(self.center.x, self.center.y),
                             Velocity(self.velocity.dx, self.velocity .dy + 2, MEDIUM_ROCK_SPIN))
        debris2 = MediumRock(Point(self.center.x, self.center.y),
                             Velocity(self.velocity.dx, self.velocity .dy - 2, MEDIUM_ROCK_SPIN))
        debris3 = SmallRock(Point(self.center.x, self.center.y),
                            Velocity(self.velocity.dx + 5, self.velocity .dy, SMALL_ROCK_SPIN))
        self.kill()

        return [debris1, debris2, debris3]


class MediumRock(Rock):
    """
    A medium flying Rock object
    """
    def __init__(self, center, velocity):
        """
        Initialize a MediumRock
        :param center: Point object
        :param velocity: Velocity object
        """
        super().__init__(center=center,
                         velocity=velocity,
                         radius=MEDIUM_ROCK_RADIUS)

    def draw(self):
        """
        Draw a MediumRock object on the screen
        :return:
        """
        super().draw('images/meteorGrey_med1.png')

    def break_apart(self):
        """
        Define what happens when something collides with a MediumRock object
        :return: a list of smaller Rock objects
        """
        debris1 = SmallRock(Point(self.center.x, self.center.y),
                            Velocity(self.velocity.dx + 1.5, self.velocity .dy + 1.5, SMALL_ROCK_SPIN))
        debris2 = SmallRock(Point(self.center.x, self.center.y),
                            Velocity(self.velocity.dx - 1.5, self.velocity .dy - 1.5, SMALL_ROCK_SPIN))

        self.kill()

        return [debris1, debris2]


class SmallRock(Rock):
    """
    A small flying Rock object
    """
    def __init__(self, center, velocity):
        """
        Initialize a SmallRock object
        :param center: Point object
        :param velocity: Velocity object
        """
        super().__init__(center=center,
                         velocity=velocity,
                         radius=SMALL_ROCK_RADIUS)

    def draw(self):
        """
        Draw a SmallRock object on the screen
        :return:
        """
        super().draw('images/meteorGrey_small1.png')

    def break_apart(self):
        """
        When something collides with a small rock, that rock should be removed
        from the game and leave no debris behind.
        :return:
        """
        self.kill()
        return []
