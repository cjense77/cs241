"""
File: pong.py
Original Author: Br. Burton
Modified by: Colin Jensen
Designed to be completed by others
This program implements a simplistic version of the
classic Pong arcade game.
"""
import arcade
import random

# These are Global constants to use throughout the game
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
BALL_RADIUS = 10

PADDLE_WIDTH = 10
PADDLE_HEIGHT = 50
MOVE_AMOUNT = 5

SCORE_HIT = 1
SCORE_MISS = 5

class Point:
    """
    This class stores an x and y coordinate for an object
    on the game screen.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Velocity:
    """
    This class stores an x and y velocity for a moving
    object.
    """

    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy

class Ball:
    """
    This class implements a Pong ball. It will look like a
    classic Pac-Man.
    """

    def __init__(self):
        """
        Sets up a Pong ball
        """

        self.center = Point(0, random.uniform(0, SCREEN_HEIGHT))
        self.velocity = Velocity(random.uniform(4, 5),
                                 random.choice([random.uniform(-4, -1), random.uniform(1,4)]))
        self.start_angle = -45
        self.end_angle = 45
        self.mouth_closing = True

    def draw(self):
        """
        Draw the Pong ball to look like Pac-Man
        :return:
        """
        arcade.draw_circle_outline(self.center.x,
                                   self.center.y,
                                   color=arcade.color.BLACK,
                                   radius=10)
        arcade.draw_circle_filled(self.center.x,
                                  self.center.y,
                                  color=arcade.color.YELLOW,
                                  radius=9)
        arcade.draw_circle_filled(self.center.x + 1,
                                  self.center.y + 4.5,
                                  radius=1.5,
                                  color=arcade.color.BLACK)
        arcade.draw_arc_filled(self.center.x,
                               self.center.y,
                               10, 10,
                               arcade.color.BLACK,
                               self.start_angle, self.end_angle, 0)

    def advance(self):
        """
        Update the ball's appearance and position
        :return:
        """
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

        # Close the mouth
        if self.mouth_closing:
            self.start_angle += 2
            self.end_angle -= 2

        # Open the mouth
        else:
            self.start_angle -= 2
            self.end_angle += 2

    def bounce_horizontal(self):
        """
        Change the ball's horizontal direction.
        :return:
        """
        self.velocity.dx *= -1

    def bounce_vertical(self):
        """
        Change the ball's vertical direction.
        :return:
        """
        self.velocity.dy *= -1

    def restart(self):
        self.__init__()

class Paddle:
    def __init__(self):
        """
        Sets up a Pong paddle
        """
        self.center = Point(SCREEN_WIDTH, SCREEN_HEIGHT / 2)

    def draw(self):
        """
        Draw the Pong paddle
        :return:
        """
        arcade.draw_rectangle_filled(self.center.x,
                                     self.center.y,
                                     PADDLE_WIDTH,
                                     PADDLE_HEIGHT,
                                     arcade.color.WHITE)

    def move_up(self):
        """
        Move the paddle up if we're still on the screen
        :return:
        """
        if self.center.y < (SCREEN_HEIGHT - PADDLE_HEIGHT/2):
            self.center.y += MOVE_AMOUNT

    def move_down(self):
        """
        Move the paddle down if we're still on the screen
        """
        if self.center.y > (PADDLE_HEIGHT/2):
            self.center.y -= MOVE_AMOUNT



class Pong(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    It assumes the following classes exist:
        Point
        Velocity
        Ball
        Paddle
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class,
    but should not have to if you don't want to.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)

        self.ball = Ball()
        self.paddle = Paddle()
        self.score = 0

        # These are used to see if the user is
        # holding down the arrow keys
        self.holding_left = False
        self.holding_right = False

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsiblity of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # draw each object
        self.ball.draw()
        self.paddle.draw()

        self.draw_score()

    def draw_score(self):
        """
        Puts the current score on the screen
        """
        score_text = "Score: {}".format(self.score)
        start_x = 10
        start_y = SCREEN_HEIGHT - 20
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=12, color=arcade.color.SKY_BLUE)

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """

        # Move the ball forward one element in time
        if self.ball.start_angle >= 0:
            self.ball.mouth_closing = False
        elif self.ball.start_angle < -45:
            self.ball.mouth_closing = True
        self.ball.advance()


        # Check to see if keys are being held, and then
        # take appropriate action
        self.check_keys()

        # check for ball at important places
        self.check_miss()
        self.check_hit()
        self.check_bounce()

    def check_hit(self):
        """
        Checks to see if the ball has hit the paddle
        and if so, calls its bounce method.
        :return:
        """
        too_close_x = (PADDLE_WIDTH / 2) + BALL_RADIUS
        too_close_y = (PADDLE_HEIGHT / 2) + BALL_RADIUS

        if (abs(self.ball.center.x - self.paddle.center.x) < too_close_x and
                    abs(self.ball.center.y - self.paddle.center.y) < too_close_y and
                    self.ball.velocity.dx > 0):
            # we are too close and moving right, this is a hit!
            self.ball.bounce_horizontal()
            self.score += SCORE_HIT

    def check_miss(self):
        """
        Checks to see if the ball went past the paddle
        and if so, restarts it.
        """
        if self.ball.center.x > SCREEN_WIDTH:
            # We missed!
            self.score -= SCORE_MISS
            self.ball.restart()

    def check_bounce(self):
        """
        Checks to see if the ball has hit the borders
        of the screen and if so, calls its bounce methods.
        """
        if self.ball.center.x < 0 and self.ball.velocity.dx < 0:
            self.ball.bounce_horizontal()

        if self.ball.center.y < 0 and self.ball.velocity.dy < 0:
            self.ball.bounce_vertical()

        if self.ball.center.y > SCREEN_HEIGHT and self.ball.velocity.dy > 0:
            self.ball.bounce_vertical()

    def check_keys(self):
        """
        Checks to see if the user is holding down an
        arrow key, and if so, takes appropriate action.
        """
        if self.holding_left:
            self.paddle.move_down()

        if self.holding_right:
            self.paddle.move_up()

    def on_key_press(self, key, key_modifiers):
        """
        Called when a key is pressed. Sets the state of
        holding an arrow key.
        :param key: The key that was pressed
        :param key_modifiers: Things like shift, ctrl, etc
        """
        if key == arcade.key.LEFT or key == arcade.key.DOWN:
            self.holding_left = True

        if key == arcade.key.RIGHT or key == arcade.key.UP:
            self.holding_right = True

    def on_key_release(self, key, key_modifiers):
        """
        Called when a key is released. Sets the state of
        the arrow key as being not held anymore.
        :param key: The key that was pressed
        :param key_modifiers: Things like shift, ctrl, etc
        """
        if key == arcade.key.LEFT or key == arcade.key.DOWN:
            self.holding_left = False

        if key == arcade.key.RIGHT or key == arcade.key.UP:
            self.holding_right = False

# Creates the game and starts it going
window = Pong(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()