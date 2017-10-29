"""
File: bullet.py
Author: Colin Jensen
Contains class for bullets to be implemented in a shooting game.
"""

from flying_object import FlyingObject
import arcade
import math

BULLET_RADIUS = 3
BULLET_COLOR = arcade.color.BLACK_OLIVE
BULLET_SPEED = 10


class Bullet(FlyingObject):
    """
    Class for a bullet in skeet shooting game
    """
    def __init__(self):
        """
        Initialize bullet
        """
        super().__init__(dx=BULLET_SPEED, dy=BULLET_SPEED)
        self.radius = BULLET_RADIUS
        self.alive = True
        self.color = BULLET_COLOR

    def draw(self):
        """
        Draw a bullet as a filled circle
        :return:
        """
        arcade.draw_circle_filled(self.center.x,
                                  self.center.y,
                                  self.radius,
                                  self.color)

    def fire(self, angle):
        """
        Define the correct direction for a bullet based on the given angle
        :param angle:
        :return:
        """
        angle = math.radians(angle)
        self.velocity.dx = BULLET_SPEED * math.cos(angle)
        self.velocity.dy = BULLET_SPEED * math.sin(angle)
