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
    def __init__(self, center, velocity, angle=0):
        """
        Initialize bullet
        """
        super().__init__(center=center, velocity=velocity, angle=angle)
        self.life = BULLET_LIFE

        self.fire()

    def draw(self):
        """
        Draw a bullet from an image file
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

    def advance(self, screen_width, screen_height):
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
