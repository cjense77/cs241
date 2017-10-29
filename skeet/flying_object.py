"""
File: flying_object.py
Author: Colin Jensen
Contains an abstract class for a flying object in an arcade game
"""

from point import Point
from velocity import Velocity
from abc import ABC
from abc import abstractmethod


class FlyingObject(ABC):
    """
    Define an abstract flying object
    """
    def __init__(self, x=0, y=0, dx=1, dy=1):
        """
        Initialize flying object
        :param x:
        :param y:
        :param dx:
        :param dy:
        """
        self.center = Point(x, y)
        self.velocity = Velocity(dx, dy)

    def advance(self):
        """
        Move the object across the screen according to its velocity
        :return:
        """
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    def is_off_screen(self, screen_width, screen_height):
        """
        Check to see if the object has moved off the screen
        :param screen_width:
        :param screen_height:
        :return:
        """
        if (self.center.x < 0 or
            self.center.x > screen_width or
            self.center.y < 0 or
            self.center.y > screen_height):
            return True
        else:
            return False

    @abstractmethod
    def draw(self):
        pass
