"""
File: skeet.py
Original Author: Br. Burton
Designed to be completed by others
This program implements an awesome version of skeet.
"""
import arcade
import math
import random
from rifle import Rifle
from bullet import Bullet
from missile import Missile
from target import *

# These are Global constants to use throughout the game
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500


class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    It assumes the following classes exist:
        Rifle
        Target (and it's sub-classes)
        Point
        Velocity
        Bullet
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class, but mostly
    you shouldn't have to. There are a few sections that you
    must add code to.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)

        self.rifle = Rifle()
        self.score = 0

        self.bullets = []

        # Create a list for targets
        self.targets = []

        self.missiles = []

        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # draw each object
        self.rifle.draw()

        for bullet in self.bullets:
            bullet.draw()

        # Iterate through the targets and draw them
        for target in self.targets:
            target.draw()

        for missile in self.missiles:
            missile.draw()

        self.draw_score()
        self.draw_instructions()

    def draw_score(self):
        """
        Puts the current score on the screen
        """
        score_text = "Score: {}".format(self.score)
        start_x = 10
        start_y = SCREEN_HEIGHT - 20
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=12, color=arcade.color.NAVY_BLUE)

    def draw_instructions(self):
        instruction_text = 'HOLD SHIFT TO DEPLOY HEAT-SEEKING MISSILE!'
        start_x = SCREEN_WIDTH / 4
        start_y = SCREEN_HEIGHT - 20
        arcade.draw_text(instruction_text, start_x=start_x, start_y=start_y, font_size=12, color=arcade.color.NAVY_BLUE)

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_collisions()
        self.check_off_screen()

        # decide if we should start a target
        if random.randint(1, 50) == 1:
            self.create_target()

        for bullet in self.bullets:
            bullet.advance()

        # Iterate through targets and tell them to advance
        for target in self.targets:
            target.advance()

        for missile in self.missiles:
            # If targets are present, hunt them down. Otherwise act like a regular bullet.
            if len(self.targets) > 0:
                distances = [self._get_distance_between_points(missile, target) for target in self.targets]
                prey_index = distances.index(min(distances))
                prey = self.targets[prey_index]
                missile.heat_seek_mode(prey, min(distances))
            else:
                missile.advance()

    def create_target(self):
        """
        Creates a new target of a random type and adds it to the list.
        :return:
        """

        # List of possible target types
        target_type = [NormalTarget, SafeTarget, StrongTarget]

        # Choose a type of target at random and create it
        target = random.choice(target_type)(screen_height=SCREEN_HEIGHT)

        self.targets.append(target)

    def check_collisions(self):
        """
        Checks to see if bullets have hit targets.
        Updates scores and removes dead items.
        :return:
        """

        # NOTE: This assumes you named your targets list "targets"

        for bullet in self.bullets:
            for target in self.targets:

                # Make sure they are both alive before checking for a collision
                if bullet.alive and target.alive:
                    too_close = bullet.radius + target.radius

                    if (abs(bullet.center.x - target.center.x) < too_close and
                        abs(bullet.center.y - target.center.y) < too_close):
                        # its a hit!
                        bullet.alive = False
                        self.score += target.hit()

        for missile in self.missiles:
            for target in self.targets:

                # Make sure they are both alive before checking for a collision
                if missile.alive and target.alive:
                    too_close = missile.radius + target.radius

                    if (abs(missile.center.x - target.center.x) < too_close and
                                abs(missile.center.y - target.center.y) < too_close):
                        # its a hit!
                        missile.alive = False
                        self.score += target.hit()

                        # We will wait to remove the dead objects until after we
                        # finish going through the list

        # Now, check for anything that is dead, and remove it
        self.cleanup_zombies()

    def cleanup_zombies(self):
        """
        Removes any dead bullets or targets from the list.
        :return:
        """
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)

        for target in self.targets:
            if not target.alive:
                self.targets.remove(target)

        for missile in self.missiles:
            if not missile.alive:
                self.missiles.remove(missile)

    def check_off_screen(self):
        """
        Checks to see if bullets or targets have left the screen
        and if so, removes them from their lists.
        :return:
        """
        for bullet in self.bullets:
            if bullet.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
                self.bullets.remove(bullet)

        for target in self.targets:
            if target.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
                self.targets.remove(target)

        for missile in self.missiles:
            if missile.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
                self.missiles.remove(missile)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        # set the rifle angle in degrees
        self.rifle.angle = self._get_angle_degrees(x, y)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        # Fire!
        angle = self._get_angle_degrees(x, y)

        if modifiers == arcade.key.MOD_SHIFT:
            missile = Missile()
            missile.fire(angle)
            self.missiles.append(missile)
        else:
            bullet = Bullet()
            bullet.fire(angle)
            self.bullets.append(bullet)

    def _get_angle_degrees(self, x, y):
        """
        Gets the value of an angle (in degrees) defined
        by the provided x and y.
        Note: This could be a static method, but we haven't
        discussed them yet...
        """
        # get the angle in radians
        angle_radians = math.atan2(y, x)

        # convert to degrees
        angle_degrees = math.degrees(angle_radians)

        return angle_degrees

    def _get_distance_between_points(self, p1, p2):
        """
        Return the Cartesian distance between two object with
        x and y coordinates.
        :param p1:
        :param p2:
        :return:
        """
        return math.sqrt((p2.center.x - p1.center.x)**2 +
                         (p2.center.y - p1.center.y)**2)

# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()
