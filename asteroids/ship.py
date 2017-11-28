"""
File: ship.py
Author: Colin Jensen
Contains a class for a flying spaceship in an arcade game
"""

from flying_object import FlyingObject
from point import Point
import math

SHIP_TURN_AMOUNT = 3
SHIP_THRUST_AMOUNT = 0.25
SHIP_RADIUS = 30


class Ship(FlyingObject):
    """
    Class for a spaceship in an arcade game
    """
    def __init__(self, screen_width=800, screen_height=600):
        """
        Initialize a ship object
        :param screen_width: int
        :param screen_height: int
        """
        super().__init__(center=Point(screen_width/2, screen_height/2),
                         angle=90,
                         radius=SHIP_RADIUS)

    def draw(self):
        """
        Draw the ship object on the screen
        :return:
        """
        super().draw('images/playerShip1_orange.png', angle=self.angle - 90)

    def apply_thrust(self, direction=1):
        """
        Apply thrust to a Ship object's velocity
        :param direction: int
        :return:
        """
        self.velocity.dx += SHIP_THRUST_AMOUNT * math.cos(math.radians(self.angle)) * direction
        self.velocity.dy += SHIP_THRUST_AMOUNT * math.sin(math.radians(self.angle)) * direction

    def turn(self, direction):
        """
        Adjust the direction a Ship object is pointing
        :param direction:
        :return:
        """
        self.angle += direction * SHIP_TURN_AMOUNT
