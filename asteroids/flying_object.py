"""
File: flying_object.py
Author: Colin Jensen
Contains an abstract class for a flying object in an arcade game
"""

from point import Point
from velocity import Velocity
from abc import ABC
import arcade


class FlyingObject(ABC):
    """
    Define an abstract flying object
    """
    def __init__(self, center=Point(), velocity=Velocity(), radius=10, angle=0):
        """
        Initialize flying object
        :param center: Point object
        :param velocity: Velocity object
        :param radius: int
        :param angle: int in degrees
        """
        self._center = center
        self._velocity = velocity
        self._radius = radius
        self._angle = angle
        self._alive = True

    @property
    def center(self):
        return self._center

    @property
    def velocity(self):
        return self._velocity

    @property
    def radius(self):
        return self._radius

    @property
    def angle(self):
        return self._angle

    @property
    def alive(self):
        return self._alive

    @center.setter
    def center(self, new_val):
        self._center = new_val

    @velocity.setter
    def velocity(self, new_val):
        self._velocity = new_val

    @radius.setter
    def radius(self, new_val):
        self._radius = new_val

    @angle.setter
    def angle(self, new_val):
        if not 0 < new_val < 360:
            self._angle = new_val % 360
        else:
            self._angle = new_val

    @alive.setter
    def alive(self, new_val):
        self._alive = new_val

    def advance(self, screen_width, screen_height):
        """
        Move the object across the screen according to its velocity
        :return:
        """
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy
        self.angle += self.velocity.da

        # Handle objects that go off the screen
        self.wrap(screen_width, screen_height)

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

    def wrap(self, screen_width, screen_height):
        """
        If a FlyingObject has moved off the screen, wrap it around to the
        other side of the screen.
        :param screen_width: int
        :param screen_height: int
        :return:
        """
        if self.is_off_screen(screen_width, screen_height):
            if self.center.x < 0:
                self.center.x = screen_width
            elif self.center.x > screen_width:
                self.center.x = 0
            elif self.center.y < 0:
                self.center.y = screen_height
            elif self.center.y > screen_height:
                self.center.y = 0

    def kill(self):
        """
        Set the FlyingObject's alive status to False
        :return:
        """
        self.alive = False

    def draw(self, image, angle='unset'):
        if angle == 'unset':
            angle = self.angle

        imgage = image
        texture = arcade.load_texture(imgage)

        width = texture.width
        height = texture.height

        arcade.draw_texture_rectangle(self.center.x,
                                      self.center.y,
                                      width,
                                      height,
                                      texture,
                                      angle)
