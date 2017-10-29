"""
File: rifle.py
Author: Bro. Burton
Contains a class for an arcade game rifle.
"""

import arcade
from point import Point

RIFLE_WIDTH = 100
RIFLE_HEIGHT = 20
RIFLE_COLOR = arcade.color.DARK_RED


class Rifle:
    """
    The rifle is a rectangle that tracks the mouse.
    """
    def __init__(self):
        """
        Initialize rifle
        """
        self.center = Point()
        self.center.x = 0
        self.center.y = 0

        self.angle = 45

    def draw(self):
        """
        Draw the rifle on the screen
        :return:
        """
        arcade.draw_rectangle_filled(self.center.x,
                                     self.center.y,
                                     RIFLE_WIDTH,
                                     RIFLE_HEIGHT,
                                     RIFLE_COLOR,
                                     self.angle)
