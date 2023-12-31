from turtle import Turtle, Screen
from game_objects import Paddle, GameScreen, Ball
from time import sleep
from random import randint

def draw_midpoint():
    """Draws midpoint of screen"""
    # Define turtle
    drawer_turtle = Turtle()

    # Set starting parameters
    drawer_turtle.hideturtle()
    drawer_turtle.color("white")

    # Draw middle
    drawer_turtle.penup()
    drawer_turtle.goto(x=0, y=screen.height/2)
    drawer_turtle.pendown()
    drawer_turtle.goto(x=0, y=-screen.height/2)


def draw_border():
    """Draws borders of game"""

    # Define turtle
    drawer_turtle = Turtle()

    # Set starting parameters
    drawer_turtle.hideturtle()
    drawer_turtle.color("white")

    # Draw bottom border
    drawer_turtle.penup()
    drawer_turtle.goto(x=-screen.width/2, y=-screen.height/2)
    drawer_turtle.pendown()
    drawer_turtle.goto(x=screen.width/2, y=-screen.height/2)

    # Draw upper border
    drawer_turtle.penup()
    drawer_turtle.goto(x=-screen.width/2, y=screen.height/2)
    drawer_turtle.pendown()
    drawer_turtle.goto(x=screen.width/2, y=screen.height/2)


def draw_score():
    score_turtle.clear()

    # Get to position to write player score
    score_turtle.penup()
    score_turtle.goto(x=-screen.width/3.5, y=screen.height/4)
    score_turtle.pendown()

    # Write score
    score_turtle.write(arg=player_paddle.score, font=("aharoni", 80, "normal"))

    # Get to position to write enemy score
    score_turtle.penup()
    score_turtle.goto(x=screen.width/3.5, y=screen.height/4)
    score_turtle.pendown()

    # Write score
    score_turtle.write(arg=enemy_paddle.score, font=("aharoni", 80, "normal"))

def detect_edge():
    """Detects ball hitting the horizontal edges of the screen"""
    if ball.y >= screen.height/2 or ball.y <= -screen.height/2:
        ball.angle = 180 - ball.angle
        ball.calculate_next_step()


def detect_paddle():
    """Detects ball hitting the paddles"""
    global speed_factor

    # Detect collision between paddle and ball based on distance and add a bit of x value to prevent weird interactions
    if abs(ball.y - enemy_paddle.y) <= 43 and abs(ball.x - enemy_paddle.x) < 15:
        ball.angle = -ball.angle
        ball.x -= 5
        speed_factor -= speed_factor/10

    elif abs(ball.y - player_paddle.y) <= 43 and abs(ball.x - player_paddle.x) < 15:
        ball.angle = -ball.angle
        ball.x += 5
        speed_factor -= speed_factor/10
    return speed_factor


def detect_goal():
    """Detects goals and updates score"""
    global speed_factor
    if ball.x >= screen.width/2:
        player_paddle.score += 1
        ball.reset_ball()
        draw_score()
        speed_factor = 0.005

    elif ball.x <= -screen.width/2:
        enemy_paddle.score += 1
        ball.reset_ball()
        draw_score()
        speed_factor = 0.005


def move_enemy():
    """Moves enemy based on ball height"""
    if enemy_paddle.y - ball.y > 0:
        enemy_paddle.y -= 1
        enemy_paddle.goto()
        enemy_paddle.turtle.clear()
        enemy_paddle.draw()

    elif enemy_paddle.y - ball.y < 0:
        enemy_paddle.y += 1
        enemy_paddle.goto()
        enemy_paddle.turtle.clear()
        enemy_paddle.draw()
def setup():
    global ball
    global player_paddle
    global enemy_paddle
    global screen
    global score_turtle
    global speed_factor

    # Setup screen stuff
    screen = GameScreen(width=854, height=525)

    # Define game elements
    player_paddle = Paddle(x=int(-screen.width / 2 + 20), y=0, score=0)
    enemy_paddle = Paddle(x=int(screen.width / 2 - 20), y=0, score=0)
    ball = Ball(x=0, y=0, angle=0)

    # Set starting speed
    speed_factor = 0.005

    # Set up turtle to draw score
    score_turtle = Turtle()
    score_turtle.hideturtle()
    score_turtle.penup()
    score_turtle.color("white")

    # Initializing game elements
    screen.initialize_screen(player_paddle=player_paddle)
    player_paddle.initialize()
    enemy_paddle.initialize()
    ball.initialize()
    draw_midpoint()
    draw_border()
    draw_score()


def maingame():
    setup()
    global speed_factor

    while True:
        # Update screen
        screen.screen.update()

        # Delay
        sleep(speed_factor)

        # Calculate steps and collision
        ball.calculate_next_step()
        move_enemy()
        detect_edge()
        detect_paddle()
        detect_goal()


maingame()