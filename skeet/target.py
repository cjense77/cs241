from flying_object import FlyingObject
import arcade
import random as rd
from abc import ABC
from abc import abstractmethod

class Target(FlyingObject, ABC):
    def __init__(self, alive=True, screen_height=500):
        super().__init__(x=0,
                         y=rd.uniform(screen_height / 2, screen_height),
                         dx=rd.uniform(1, 5),
                         dy=rd.uniform(-2, 5))
        self.alive = alive

    @abstractmethod
    def advance(self):
        super().advance()

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def is_off_screen(self, screen_width, screen_height):
        if (self.center.x < 0 or
            self.center.x > screen_width or
            self.center.y < 0 or
            self.center.y > screen_height):
            return True
        else:
            return False

class NormalTarget(Target):
    def __init__(self, radius = 20, alive = True, screen_height = 500):
        super().__init__(x=0, y=rd.uniform(screen_height/2, screen_height),
                         dx=rd.uniform(1,5), dy=rd.uniform(-2,5))
        self.radius = radius
        self.alive = alive

    def advance(self):
        super().advance()

    def draw(self):
        arcade.draw_circle_filled(self.center.x,
                                  self.center.y,
                                  self.radius,
                                  arcade.color.DARK_RASPBERRY)

    def is_off_screen(self, screen_width, screen_height):
        super().is_off_screen

    def hit(self):
        return 1
