from flying_object import FlyingObject
import arcade
import math

BULLET_RADIUS = 3
BULLET_COLOR = arcade.color.BLACK_OLIVE
BULLET_SPEED = 10

class Bullet(FlyingObject):
    def __init__(self):
        super().__init__(dx=BULLET_SPEED, dy=BULLET_SPEED)
        self.radius = BULLET_RADIUS
        self.alive = True

    def advance(self):
        super().advance()

    def draw(self):
        arcade.draw_circle_filled(self.center.x,
                                  self.center.y,
                                  BULLET_RADIUS,
                                  BULLET_COLOR)

    def is_off_screen(self, screen_width, screen_height):
        if (self.center.x < 0 or
            self.center.x > screen_width or
            self.center.y < 0 or
            self.center.y > screen_height):
            return True
        else:
            return False

    def fire(self, angle):
        angle = math.radians(angle)
        self.velocity.dx = BULLET_SPEED * math.cos(angle)
        self.velocity.dy = BULLET_SPEED * math.sin(angle)