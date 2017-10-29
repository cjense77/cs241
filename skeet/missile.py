from flying_object import FlyingObject
import arcade
import math

MISSILE_SPEED = 5
MISSILE_RADIUS = 15

class Missile(FlyingObject):
    def __init__(self):
        super().__init__()
        self.alive = True
        self.radius = MISSILE_RADIUS

    def draw(self):
        arcade.draw_parabola_filled(self.center.x,
                                    self.center.y,
                                    self.center.x + 5,
                                    self.radius,
                                    arcade.color.RED_DEVIL)
    def fire(self, angle):
        """
        Define the correct direction for a bullet based on the given angle
        :param angle:
        :return:
        """
        angle = math.radians(angle)
        self.velocity.dx = MISSILE_SPEED * math.cos(angle)
        self.velocity.dy = MISSILE_SPEED * math.sin(angle)
