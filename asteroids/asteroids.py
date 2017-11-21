"""
File: asteroids.py
Original Author: Br. Burton
Designed to be completed by others
This program implements the asteroids game.
"""
import arcade
from bullet import Bullet
from ship import Ship
from rocks import *
from point import Point
from velocity import Velocity


# These are Global constants to use throughout the game
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

INITIAL_ROCK_COUNT = 5


class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.SMOKY_BLACK)

        self.held_keys = set()

        # TODO: declare anything here you need the game class to track
        self.ship = Ship(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.rocks = [BigRock(SCREEN_WIDTH, SCREEN_HEIGHT) for i in range(5)]
        self.bullets = []

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # TODO: draw each object
        if self.ship.alive:
            self.ship.draw()

        for rock in self.rocks:
            rock.draw()

        for bullet in self.bullets:
            bullet.draw()

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_keys()

        # TODO: Tell everything to advance or move forward one step in time
        self.ship.advance(SCREEN_WIDTH, SCREEN_HEIGHT)

        for rock in self.rocks:
            rock.advance(SCREEN_WIDTH, SCREEN_HEIGHT)

        for bullet in self.bullets:
            bullet.advance(SCREEN_WIDTH, SCREEN_HEIGHT)

        # TODO: Check for collisions
        self.check_collision()
        self.clear_zombies()

    def check_collision(self):
        for rock in self.rocks:
            if self._has_collided(rock, self.ship):
                self.ship.kill()
                debris = rock.break_apart()
                self.rocks.extend(debris)

            for bullet in self.bullets:
                if self._has_collided(rock, bullet):
                    debris = rock.break_apart()
                    self.rocks.extend(debris)
                    bullet.kill()

    def _has_collided(self, obj1, obj2):
        if obj1.alive and obj2.alive:
            too_close = obj1.radius + obj2.radius

            if (abs(obj1.center.x - obj2.center.x) < too_close and
                        abs(obj1.center.y - obj2.center.y) < too_close):
                # its a hit!
                return True
        return False

    def clear_zombies(self):
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)
        for rock in self.rocks:
            if not rock.alive:
                self.rocks.remove(rock)

    def check_keys(self):
        """
        This function checks for keys that are being held down.
        You will need to put your own method calls in here.
        """
        if arcade.key.LEFT in self.held_keys:
            self.ship.turn(1)

        if arcade.key.RIGHT in self.held_keys:
            self.ship.turn(-1)

        if arcade.key.UP in self.held_keys:
            self.ship.apply_thrust()

        if arcade.key.DOWN in self.held_keys:
            self.ship.apply_thrust(-1)

        # Machine gun mode...
        #if arcade.key.SPACE in self.held_keys:
        #    pass


    def on_key_press(self, key: int, modifiers: int):
        """
        Puts the current key in the set of keys that are being held.
        You will need to add things here to handle firing the bullet.
        """
        if self.ship.alive:
            self.held_keys.add(key)

            if key == arcade.key.SPACE:
                # TODO: Fire the bullet here!
                bullet = Bullet(Point(x=self.ship.center.x, y=self.ship.center.y),
                                Velocity(dx=self.ship.velocity.dx, dy=self.ship.velocity.dy),
                                angle=self.ship.angle)
                self.bullets.append(bullet)

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)


# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()
