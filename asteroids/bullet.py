"""
File: bullet.py
Author: Colin Jensen
Contains class for bullets to be implemented in a shooting game.
"""

from flying_object import FlyingObject
import arcade
import math

BULLET_RADIUS = 30
BULLET_SPEED = 10
BULLET_LIFE = 60


class Bullet(FlyingObject):
    """
    Class for a bullet in skeet shooting game
    """
    def __init__(self, x=0, y=0, dx=0, dy=0, angle=0):
        """
        Initialize bullet
        """
        super().__init__(x=x, y=y,
                         dx=dx + BULLET_SPEED,
                         dy=dy + BULLET_SPEED,
                         radius=BULLET_RADIUS,
                         angle=angle)
        self.life = BULLET_LIFE

        self.fire(angle)

    def draw(self):
        """
        Draw a bullet as a filled circle
        :return:
        """
        image = 'images/laserBlue01.png'
        texture = arcade.load_texture(image)

        width = texture.width
        height = texture.height

        arcade.draw_texture_rectangle(self.center.x,
                                      self.center.y,
                                      width,
                                      height,
                                      texture,
                                      self.angle)

    def fire(self, angle):
        """
        Define the correct direction for a bullet based on the given angle
        :param angle:
        :return:
        """
        angle = math.radians(angle)
        self.velocity.dx = BULLET_SPEED * math.cos(angle)
        self.velocity.dy = BULLET_SPEED * math.sin(angle)
