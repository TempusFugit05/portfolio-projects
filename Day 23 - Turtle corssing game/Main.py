import random
from turtle import Turtle, Screen
from game_objects import Car, Player, ScoreDrawer
from time import sleep
from random import randint, randrange

# Set screen parameters
screen = Screen()
screen.setup(width=1000, height=800)
screen.tracer(0)
screen.listen()

# Key loggers
screen.onkeypress(fun=lambda max_height=1.2*screen.canvheight: player.move_forward(max_height), key="w")
screen.onkeypress(fun=lambda min_height=1.2*-screen.canvheight: player.move_backwards(min_height), key="s")

# Define player object
player = Player()

HIGH_SCORE_PATH = "high_score"
score_drawer = ScoreDrawer(x=screen.canvwidth/2, y=screen.canvheight-100, high_score=HIGH_SCORE_PATH)


def set_cars(num_cars):
    """Creates set number of cars"""
    global cars, max_car_speed, min_car_speed

    cars = []

    # Minimum y position
    starting_y = -screen.canvheight

    # Create car object for given number of cars
    for i in range(num_cars+1):

        # Create random car parameters
        cars.append(Car(size_x=1.5*screen.canvwidth/num_cars + 10, size_y=1.75*screen.canvwidth/(2*num_cars), default_y=starting_y, default_x=-1.2*screen.canvwidth, x=random.randint(-screen.canvwidth, screen.canvwidth),
                        speed=round(random.uniform(min_car_speed, max_car_speed), 2)))

        # Set starting y position
        starting_y += (2*screen.canvheight) / num_cars


def set_high_score():
    global HIGH_SCORE_PATH, score

    with open(HIGH_SCORE_PATH, mode="r") as file:
        max_score = file.read()

    with open(HIGH_SCORE_PATH, mode="w") as file:
        if score > int(max_score):
            file.write(str(score))
        else:
            file.write(str(max_score))


def win_condition(cars, player_default_y):
    """Checks if player passed road and changes values accordingly"""

    global score, car_number, time_factor, max_car_speed, score_drawer, min_car_speed

    # Checks if player got ot the end of the road
    if player.detect_win(max_height=screen.canvheight):

        # Adds score and number of cars
        score += 1
        car_number += 1
        time_factor -= time_factor/10
        max_car_speed += 0.5
        min_car_speed += 0.5

        # Checks if score bigger than high score
        set_high_score()

        # Draw score
        score_drawer.draw_score(score=score, high_score_path=HIGH_SCORE_PATH)

        # Resets player y position
        player.y = player_default_y
        player.goto()

        clear_screen(cars)

        # Generates new cars
        set_cars(car_number)

        return score, car_number, time_factor


def clear_screen(cars):
    """Clears drawing for every car"""
    for car in cars:
        car.turtle.clear()


def lose_condition():
    """Returns if player was hit"""
    for car in cars:
        if car.detect_collision(collider_x=player.x, collider_y=player.y):
            return True


def move_cars():
    """Move every car"""
    for car in cars:
        car.move()


def maingame():
    """Main function"""

    global cars, score, time_factor, is_alive, car_number, max_car_speed ,min_car_speed

    # Set initial game values
    score = 0
    car_number = 5
    time_factor = 0.01
    is_alive = True
    max_car_speed = 6
    min_car_speed = 3

    # Define default player position
    player_default_y = -1.3 * screen.canvheight

    player.y = player_default_y

    # Draw initial player position
    player.goto()

    # Create cars
    set_cars(car_number)

    # Write score
    score_drawer.draw_score(score=score, high_score_path=HIGH_SCORE_PATH)

    # Play game while player is alive
    while is_alive:

        # Update screen
        screen.update()
        sleep(0.01)

        # Detect if player won
        win_condition(cars=cars, player_default_y=player_default_y)

        move_cars()

        is_alive = not lose_condition()


maingame()
screen.exitonclick()