from flying_object import FlyingObject
from point import Point
import arcade
import math

SHIP_TURN_AMOUNT = 3
SHIP_THRUST_AMOUNT = 0.25
SHIP_RADIUS = 30


class Ship(FlyingObject):
    def __init__(self, screen_width=800, screen_height=600):
        super().__init__(center=Point(screen_width/2, screen_height/2),
                         angle=90,
                         radius=SHIP_RADIUS)

    def draw(self):
        img = 'images/playerShip1_orange.png'
        texture = arcade.load_texture(img)

        width = texture.width
        height = texture.height

        arcade.draw_texture_rectangle(self.center.x,
                                      self.center.y,
                                      width,
                                      height,
                                      texture,
                                      self.angle - 90)

    def apply_thrust(self, direction=1):
        self.velocity.dx += SHIP_THRUST_AMOUNT * math.cos(math.radians(self.angle)) * direction
        self.velocity.dy += SHIP_THRUST_AMOUNT * math.sin(math.radians(self.angle)) * direction

    def turn(self, direction):
        self.angle += direction * SHIP_TURN_AMOUNT
