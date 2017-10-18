from flying_object import *
import arcade
import random as rd

class Target(FlyingObject):
    def __init__(self, radius = 10, alive = True, screen_height = 500):
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
        if (self.center.x < 0 or
            self.center.x > screen_width or
            self.center.y < 0 or
            self.center.y > screen_height):
            return True
        else:
            return False

    def hit(self):
        return 1
