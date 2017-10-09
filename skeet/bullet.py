from flying_object import *

BULLET_RADIUS = 3
BULLET_COLOR = arcade.color.BLACK_OLIVE
BULLET_SPEED = 10

class Bullet(FlyingObject):
    def __init__(self):
        super().__init__()
        self.radius = BULLET_RADIUS

    def advance(self):
        pass

    def draw(self):
        pass

    def is_off_screen(self):
        pass

    def fire(self):
        pass
