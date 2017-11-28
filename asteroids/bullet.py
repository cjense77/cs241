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
    Class for a bullet in a shooting game
    """
    def __init__(self, center, velocity, angle=0, radius=BULLET_RADIUS):
        """
        Initialize a Bullet object
        :param center: Point object
        :param velocity: Velocity object
        :param angle: int angle in degrees
        """
        super().__init__(center=center,
                         velocity=velocity,
                         angle=angle,
                         radius=radius)
        self.life = BULLET_LIFE

        self.fire()

    def draw(self, image='unset'):
        """
        Draw a bullet from an image file
        :return:
        """
        if image == 'unset':
            image = 'images/laserBlue01.png'
        super().draw(image)

    def advance(self, screen_width, screen_height):
        """
        Advance a Bullet object across the screen
        :param screen_width: int
        :param screen_height: int
        :return:
        """
        super().advance(screen_width, screen_height)

        self.life -= 1
        if self.life < 1:
            self.kill()

    def fire(self):
        """
        Define the correct direction for a bullet based on the given angle
        :return:
        """
        angle = math.radians(self.angle)

        self.velocity.dx += BULLET_SPEED * math.cos(angle)
        self.velocity.dy += BULLET_SPEED * math.sin(angle)
