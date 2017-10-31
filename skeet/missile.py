"""
File: missile.py
Author: Colin Jensen
Contains a class for a 'heat-seeking' missile for an
arcade game
"""

from flying_object import FlyingObject
import arcade
import math

MISSILE_SPEED = 8
MISSILE_RADIUS = 5


class Missile(FlyingObject):
    """
    Class for a 'heat-seeking' missile
    """
    def __init__(self):
        """
        Initialize the missile
        """
        super().__init__()
        self.alive = True
        self.radius = MISSILE_RADIUS
        self.tilt = 0
        self.speed = MISSILE_SPEED

    def draw(self):
        """
        Draw the missile on the screen
        :return:
        """
        arcade.draw_parabola_filled(self.center.x,
                                    self.center.y,
                                    self.center.x + 5,
                                    self.radius * 3,
                                    arcade.color.RED_DEVIL,
                                    self.tilt)

    def heat_seek_mode(self, prey, distance):
        """
        If there are targets to hit (ie a prey), then alter x and y
        components of velocity to seek the prey
        :param prey:
        :param distance:
        :return:
        """
        super().advance()
        angle = math.degrees(math.atan2(prey.center.y, prey.center.x))

        # Change the missile's velocity to follow the prey
        self.fire(angle)

        # Alter the speed of the missile according to how far away the prey is
        self.speed = -0.019*distance + 20



    def fire(self, angle):
        """
        Define the correct direction for a bullet based on the given angle
        :param angle:
        :return:
        """
        self.tilt = angle - 90
        angle = math.radians(angle)
        self.velocity.dx = self.speed * math.cos(angle)
        self.velocity.dy = self.speed * math.sin(angle)
