from turtle import Turtle, Screen
import math
import random

class GameScreen:
    height = 0
    width = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = Screen()

    def initialize_screen(self, player_paddle):
        # self.screen.clear()
        self.screen.setup(width=self.width, height=self.height)
        self.screen.bgcolor("black")
        self.screen.tracer(0)
        self.screen.listen()
        # Setup keyloggers
        self.screen.onkeypress(lambda key="w": self.key_logger(key, player_paddle=player_paddle), "w")
        self.screen.onkeypress(lambda key="s": self.key_logger(key, player_paddle=player_paddle), "s")

    def key_logger(self, key, player_paddle):
        player_paddle.move(key=key, screen_height=self.height)


class Base:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.turtle = Turtle()

    def goto(self):
        # Go to coordinates
        self.turtle.penup()
        self.turtle.goto(x=self.x, y=self.y)
        self.turtle.pendown()

    def initialize(self):
        # Set starting parameters, go to set position and draw paddle line
        self.turtle.width(10)
        self.turtle.color("white")
        self.turtle.hideturtle()
        self.goto()
        self.draw()


class Paddle(Base):
    x = 0
    y = 0
    score = 0

    def __init__(self, x, y, score):
        Base.__init__(self, x, y)
        self.score = score

    def draw(self):
        # Draw paddle line
        self.turtle.goto(x=self.x, y=self.y+20)
        self.turtle.goto(x=self.x, y=self.y-40)
        self.goto()

    def move(self, key, screen_height):
        # Move paddle based on key unless paddle is out of bounds

        if key == "w":

            if self.y + 45 <= screen_height/2:

                self.y += 10
                self.goto()
                self.turtle.clear()
                self.draw()

            else:

                self.y = -screen_height/2 + 40
                self.goto()
                self.turtle.clear()
                self.draw()

        elif key == "s":
            # Check if next step would be out of bounds
            if self.y - 45 >= -screen_height/2:

                self.y -= 10
                self.goto()
                self.turtle.clear()
                self.draw()

            else:

                self.y = screen_height/2 - 40
                self.y = self.y
                self.goto()
                self.turtle.clear()
                self.draw()


class Ball(Base):
    x = 0
    y = 0
    angle = 0

    def __init__(self, x, y, angle):
        Base.__init__(self, x, y)
        self.angle = angle

    def initialize(self):
        # Set starting parameters, go to set position and draw paddle line
        self.turtle.width(10)
        self.turtle.color("white")
        self.turtle.shape("circle")
        self.goto()
        self.reset_ball()

    def calculate_next_step(self):
        self.x += math.sin(math.radians(self.angle))*2
        self.y += math.cos(math.radians(self.angle))*2
        self.goto()

    def reset_ball(self):
        self.x = 0
        self.y = 0
        self.angle = random.randint(-45, 45)+270