import arcade
from point import Point

class Rifle:
    """
    The rifle is a rectangle that tracks the mouse.
    """
    def __init__(self):
        self.center = Point()
        self.center.x = 0
        self.center.y = 0

        self.angle = 45

    def draw(self):
        arcade.draw_rectangle_filled(self.center.x,
                                     self.center.y,
                                     RIFLE_WIDTH,
                                     RIFLE_HEIGHT,
                                     RIFLE_COLOR,
                                     self.angle)
