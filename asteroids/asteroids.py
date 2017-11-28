"""
File: asteroids.py
Original Author: Br. Burton
Designed to be completed by others
This program implements the asteroids game.
"""
import arcade
from bullet import Bullet
from death_blossom import DeathBlossom
from ship import Ship
from rocks import *
from point import Point
from velocity import Velocity


# These are Global constants to use throughout the game
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

DEATH_BLOSSOM_REQUIRED_SCORE = 5

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
        self.score = 0

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

        self.draw_score()
        self.draw_instructions()

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

    def draw_score(self):
        """
        Puts the current score on the screen
        """
        score_text = "Score: {}".format(self.score)
        start_x = 10
        start_y = SCREEN_HEIGHT - 20
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=12, color=arcade.color.WHITE_SMOKE)

    def draw_instructions(self):
        """
        Display instructions for user on the screen
        :return:
        """
        if not self.ship.alive:
            instruction_text = 'GAME OVER!'
        elif len(self.rocks) < 1:
            instruction_text = 'YOU HAVE SAVED THE DAY!'
        elif self.score < DEATH_BLOSSOM_REQUIRED_SCORE:
            instruction_text = 'ACHIEVE 5 POINTS TO UNLOCK DEATH BLOSSOM'
        elif self.score >= DEATH_BLOSSOM_REQUIRED_SCORE:
            instruction_text = 'HOLD SHIFT TO DEPLOY DEATH BLOSSOM!'
        start_x = SCREEN_WIDTH / 3
        start_y = SCREEN_HEIGHT - 20
        arcade.draw_text(instruction_text, start_x=start_x, start_y=start_y,
                         font_size=12, color=arcade.color.RED)

    def check_collision(self):
        """
        Run through all the flying objects in the game and check
        to see if any of them have collided
        :return:
        """
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
                    self. score += 1

    def _has_collided(self, obj1, obj2):
        """
        Decide whether or not two flying objects have collided with each other
        :param obj1: FlyingObject
        :param obj2: FlyingObject
        :return:
        """
        if obj1.alive and obj2.alive:
            too_close = obj1.radius + obj2.radius

            if (abs(obj1.center.x - obj2.center.x) < too_close and
                    abs(obj1.center.y - obj2.center.y) < too_close):
                # its a hit!
                return True
        return False

    def clear_zombies(self):
        """
        Remove all flying objects from the game that are no longer alive
        :return:
        """
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
        # if arcade.key.SPACE in self.held_keys:
        #     pass

    def on_key_press(self, key: int, modifiers: int):
        """
        Puts the current key in the set of keys that are being held.
        You will need to add things here to handle firing the bullet.
        """
        if self.ship.alive:
            self.held_keys.add(key)

            # Fire death blossom
            if (key == arcade.key.SPACE and
                    modifiers == arcade.key.MOD_SHIFT and
                    self.score >= DEATH_BLOSSOM_REQUIRED_SCORE):
                death_blossom = DeathBlossom(Point(x=self.ship.center.x, y=self.ship.center.y),
                                             Velocity(dx=self.ship.velocity.dx, dy=self.ship.velocity.dy),
                                             angle=self.ship.angle)
                self.bullets.append(death_blossom)
                self.score -= DEATH_BLOSSOM_REQUIRED_SCORE

            # Fire bullet
            elif key == arcade.key.SPACE:
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
