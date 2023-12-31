from turtle import Turtle
from random import randint


class Segment:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.segment = Turtle()
        self.x = x
        self.y = y

    def create(self):
        self.segment.shape("square")
        self.segment.color("white")

    def move(self):
        self.segment.penup()
        self.segment.goto(self.x, self.y)
        self.segment.pendown()


class Fruit:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.segment = Turtle()
        self.x = x
        self.y = y

    def create(self):
        # Initialize visuals
        self.segment.shape("circle")
        self.segment.shapesize(0.5, 0.5, 1)
        self.segment.color("purple")

    def move(self):
        # Move to xy coordinates
        self.segment.penup()
        self.segment.goto(self.x, self.y)
        self.segment.pendown()

    def generate_new_position(self, screen_width, screen_height, snake):
        """Generates new fruit position"""

        # Assign random fruit coordinates
        self.x = randint(int(-screen_width / 40) + 1, int(screen_width / 40) - 1) * 20
        self.y = randint(int(-screen_height / 40) + 1, int(screen_height / 40) - 1) * 20

        is_valid_position = False

        # Checks if fruit position is inside snake
        while not is_valid_position:

            # Check if new coordinates collide with snake
            for segment in snake:
                if segment.x == self.x and segment.y == segment.y:
                    self.generate_new_position(screen_width, screen_height, snake)

            is_valid_position = True

        # Move fruit to coordinates
        self.move()



