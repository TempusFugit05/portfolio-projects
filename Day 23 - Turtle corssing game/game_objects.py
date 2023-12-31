from turtle import Turtle, Screen


class Car:
    def __init__(self, default_x, default_y, x=None, speed=None, color=None, size_x=None, size_y=None):
        # A way to set default values is by setting the default-able parameters to None and writing an if else condition
        # That checks for the parameter value

        # Set default values
        DEFAULT_SPEED = 2
        DEFAULT_COLOR = "blue"
        DEFAULT_SIZE_X = 75
        DEFAULT_SIZE_Y = 37.5

        # Check if value should be default and set attributes accordingly
        self.speed = speed if speed is not None else DEFAULT_SPEED
        self.color = color if color is not None else DEFAULT_COLOR
        self.size_x = size_x if size_x is not None else DEFAULT_SIZE_X
        self.size_y = size_y if size_y is not None else DEFAULT_SIZE_Y
        self.turtle = Turtle()

        # Non-default-able attributes
        self.x = x if x is not None else default_x
        self.y = default_y

        self.default_x = default_x
        self.default_y = default_y


        # Set turtle parameters
        self.turtle.color(self.color)
        self.turtle.hideturtle()

    def draw_car(self):
        """Draws car rectangle"""

        # Start shape fill
        self.turtle.begin_fill()

        # Go to lower right corner
        self.turtle.penup()
        self.turtle.goto(x=self.x + self.size_x/2, y=self.y - self.size_y/2)
        self.turtle.pendown()

        # Draw up
        self.turtle.goto(x=self.x + self.size_x/2, y=self.y + self.size_y/2)

        # Draw left
        self.turtle.goto(x=self.x - self.size_x/2, y=self.y + self.size_y/2)

        # Draw down
        self.turtle.goto(x=self.x - self.size_x/2, y=self.y - self.size_y/2)

        # Go back to first point
        self.turtle.goto(x=self.x + self.size_x/2, y=self.y - self.size_y/2)
        self.turtle.end_fill()

    def goto(self):
        """Moves turtle object to new position without drawing"""
        self.turtle.penup()
        self.turtle.goto(x=self.x, y=self.y)
        self.turtle.pendown()

    def move(self):
        """Moving car to new position based on speed"""
        self.turtle.clear()
        self.x += self.speed
        self.goto()
        self.draw_car()
        self.reset_car()

    def detect_collision(self, collider_x, collider_y):
        """Detects if player is inside the bounding box of the car. Returns True if player got hit and False if not"""
        if self.x - self.size_x/2 <= collider_x <= self.x + self.size_x/2 and self.y - self.size_y/2 <= collider_y <= self.y + self.size_y/2:
            return True
        else:
            return False

    def reset_car(self):
        """Resets car position if it went out of bounds"""
        if self.x >= -self.default_x:
            self.x = self.default_x
            self.goto()


class Player:
    def __init__(self, x=None, y=None):
        # Set default parameters
        DEFAULT_X = 0
        DEFAULT_Y = 0
        self.x = x if x is not None else DEFAULT_X
        self.y = y if y is not None else DEFAULT_Y

        self.turtle = Turtle()

        # Set turtle parameters
        self.turtle.shape("turtle")
        self.turtle.color("green")
        self.turtle.seth(90)

    def goto(self):
        """Moves turtle object to new position without drawing"""
        self.turtle.penup()
        self.turtle.goto(x=self.x, y=self.y)
        self.turtle.pendown()

    def move_forward(self, max_height):
        if self.y + 15 < max_height:
            self.y += 15
            self.goto()
        else:
            self.y += max_height-self.y

    def move_backwards(self, min_height):
        if self.y - 15 > min_height:
            self.y -= 15
            self.goto()
        else:
            self.y -= min_height-self.y

    def detect_win(self, max_height):
        if self.y >= max_height-5:
            print("win")
            return True

class ScoreDrawer:
    def __init__(self, x, y, high_score):
        self.turtle = Turtle()
        self.x = x
        self.y = y
        self.high_score = high_score

    def goto(self):
        """Moves turtle object to new position without drawing"""
        self.turtle.penup()
        self.turtle.goto(x=self.x, y=self.y)
        self.turtle.pendown()

    def draw_score(self, score, high_score_path):
        # Clear and go to position
        self.turtle.clear()
        self.turtle.hideturtle()
        self.goto()

        # Write score
        with open(high_score_path) as file:
            high_score = file.read()
            self.turtle.write(arg=f"Score: {score}\nHigh Score: {high_score}", font=("aharoni", 20, "normal"))