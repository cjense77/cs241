"""
File: target.py
Author: Colin Jensen
Contains classes for various targets in an arcade game.
"""

from flying_object import FlyingObject
import arcade
import random as rd
from abc import abstractmethod


TARGET_RADIUS = 20
TARGET_COLOR = arcade.color.CARROT_ORANGE
TARGET_SAFE_COLOR = arcade.color.AIR_FORCE_BLUE
TARGET_SAFE_RADIUS = 15


class Target(FlyingObject):
    """
    Abstract class for arcade game targets
    """
    def __init__(self, screen_height):
        """
        Initialize target
        :param screen_height:
        """
        super().__init__(x=0,
                         y=rd.uniform(screen_height / 2, screen_height),
                         dx=rd.uniform(1, 5),
                         dy=rd.uniform(-2, 5))
        self.alive = True

    @abstractmethod
    def hit(self):
        pass


class NormalTarget(Target):
    """
    Class for a normal target (1 hit to kill, 1 point award)
    """
    def __init__(self, screen_height):
        """
        Initialize a normal target
        :param screen_height:
        """
        super().__init__(screen_height)
        self.color = TARGET_COLOR
        self.radius = TARGET_RADIUS

    def draw(self):
        """
        Draw a normal target
        :return:
        """
        arcade.draw_circle_filled(self.center.x,
                                  self.center.y,
                                  self.radius,
                                  self.color)

    def hit(self):
        """
        Handles the target being hit
        :return:
        """
        self.alive = False
        return 1


class SafeTarget(Target):
    """
    Class for safe target (1 hit to kill, 10 point loss for hitting)
    """
    def __init__(self, screen_height):
        """
        Initialize safe target
        :param screen_height:
        """
        super().__init__(screen_height)
        self.color = TARGET_SAFE_COLOR
        self.radius = TARGET_SAFE_RADIUS

    def draw(self):
        """
        Draw safe target
        :return:
        """
        arcade.draw_rectangle_filled(self.center.x,
                                     self.center.y,
                                     self.radius * 2,
                                     self.radius * 2,
                                     self.color)

    def hit(self):
        """
        Handle target being hit
        :return:
        """
        self.alive = False
        return -10


class StrongTarget(Target):
    """
    Class for strong target (3 hits to kill, 1 point for first hit,
    1 point for second hit, 5 point for third hit)
    """
    def __init__(self, screen_height, lives=3):
        """
        Initialize strong target
        :param screen_height:
        :param lives:
        """
        super().__init__(screen_height)
        self.color = TARGET_COLOR
        self.radius = TARGET_RADIUS
        self.lives = lives
        self.velocity.dx = rd.uniform(1, 3)
        self.velocity.dy = rd.uniform(-2, 3)

    def draw(self):
        """
        Draw strong target with number of live insdie
        :return:
        """
        arcade.draw_circle_outline(self.center.x,
                                   self.center.y,
                                   self.radius,
                                   self.color)
        arcade.draw_text(str(self.lives),
                         self.center.x,
                         self.center.y,
                         self.color)

    def hit(self):
        """
        Handle the target being hit
        :return:
        """

        # Logic for deciding how many points to award for
        # hitting the strong target
        if self.lives > 1:
            self.lives -= 1
            return 1
        else:
            self.alive = False
            return 5
