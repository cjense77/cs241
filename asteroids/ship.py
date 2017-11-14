from flying_object import FlyingObject
import arcade
import math

SHIP_TURN_AMOUNT = 3
SHIP_THRUST_AMOUNT = 0.25
SHIP_RADIUS = 30


class Ship(FlyingObject):
    def __init__(self, screen_width=800, screen_height=600):
        super().__init__(x=screen_width/2,
                         y=screen_height/2,
                         dx=0, dy=0,
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

    def apply_thrust(self):
        #self.velocity.dx += SHIP_THRUST_AMOUNT
        #self.velocity.dy += SHIP_THRUST_AMOUNT

        self.velocity.dx += SHIP_THRUST_AMOUNT * math.cos(math.radians(self.angle))
        self.velocity.dy += SHIP_THRUST_AMOUNT * math.sin(math.radians(self.angle))

    def turn(self, direction):
        self.angle += direction * SHIP_TURN_AMOUNT
