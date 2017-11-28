"""
File: death_blossom.py
Author: Colin Jensen
Contains a class for a special bullet in an arcade game. A few frames
after being fired, the death blossom explodes, destroying everything near it.
"""

from bullet import Bullet

DEATH_BLOSSOM_FUSE = 30
DEATH_BLOSSOM_RADIUS = 30

class DeathBlossom(Bullet):
    """
    A special exploding bullet for an arcade game
    """
    def __init__(self, center, velocity, angle=0):
        """
        Initialize a DeathBlossom object
        :param center: Point object
        :param velocity: Velocity Object
        :param angle: int angle in degrees
        """
        super().__init__(center, velocity, angle, DEATH_BLOSSOM_RADIUS)
        self.image = 'images/laserRed01.png'
        self.exploded = False

    def draw(self):
        """
        Draw a DeathBlossom object on the screen
        :return:
        """
        super().draw(self.image)

    def advance(self, screen_width, screen_height):
        """
        Advance a DeathBlossom object across the screen
        :param screen_width: int
        :param screen_height: int
        :return:
        """
        super().advance(screen_width, screen_height)

        if self.life < DEATH_BLOSSOM_FUSE:
            self.kill()

    def kill(self):
        """
        Carry out the explosion sequence for a DeathBlossom object
        :return:
        """
        self.image = 'images/explosion.png'
        self.radius = DEATH_BLOSSOM_RADIUS * 3
        self.velocity.dx = 0
        self.velocity.dy = 0
        if self.life < 1:
            super().kill()
