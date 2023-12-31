from turtle import Turtle, Screen
from segment import Segment, Fruit
from time import sleep

screen = Screen()

is_alive = True
snake = [Segment(60, 0), Segment(40, 0), Segment(20, 0), Segment(0, 0)]
fruits = [Fruit(0, 0)]
default_key = "w"


def draw_border():
    border_turtle = Turtle()
    border_turtle.isvisible()
    border_turtle.pensize(20)
    border_turtle.color("red")
    border_turtle.penup()
    border_turtle.goto(x=-screen.canvwidth / 2 - 20, y=screen.canvheight / 2 + 30)
    border_turtle.pendown()
    border_turtle.goto(x=screen.canvwidth / 2 + 20, y=screen.canvheight / 2 + 30)
    border_turtle.goto(x=screen.canvwidth / 2 + 20, y=-screen.canvheight / 2 - 30)
    border_turtle.goto(x=-screen.canvwidth / 2 - 20, y=-screen.canvheight / 2 - 30)
    border_turtle.goto(x=-screen.canvwidth / 2 - 20, y=screen.canvheight / 2 + 30)


def key_logger(key):
    """Changes snake direction based on keyloggers"""
    global default_key
    print(default_key)

    if can_move_head(key):
        default_key = key


def can_move_head(key):
    """Checks if head can move by checking if movement would be equal to the segment before head"""
    # Won't work for single segment*
    if key == "w":
        if snake[0].y + 20 == snake[1].y:
            return False

    elif key == "a":
        if snake[0].x - 20 == snake[1].x:
            return False

    elif key == "s":
        if snake[0].y - 20 == snake[1].y:
            return False

    else:
        if snake[0].x + 20 == snake[1].x:
            return False
    return True


def move_head(key):
    """Moves head based on key presses"""

    # Move body
    move_snake()

    # generate new coordinates based on key
    if key == "w":
        snake[0].y += 20

    elif key == "a":
        snake[0].x -= 20

    elif key == "s":
        snake[0].y -= 20

    else:
        snake[0].x += 20

    # Move head to new position
    snake[0].move()
    screen.update()


def move_snake():
    """Move each segment forward"""
    # Iterate for the length of the snake
    for i in range(1, len(snake)):
        # Assign the coordinates of the last segment to the one after it
        snake[-i].x = snake[-i - 1].x
        snake[-i].y = snake[-i - 1].y

        # Move segment to new position
        snake[-i].move()


def eat_fruit(x_pos, y_pos):
    """Checks for eaten fruit and generates new position"""
    for fruit in fruits:

        # Check if fruit position is equal to head
        if snake[0].x == fruit.x and snake[0].y == fruit.y:
            fruit.generate_new_position(screen_width=screen.canvwidth, screen_height=screen.canvheight, snake=snake)
            snake.append(Segment(x=x_pos, y=y_pos))
            snake[len(snake) - 1].create()
            print("BAZINGA!")


def snake_tail_position():
    x = snake[len(snake) - 1].x
    y = snake[len(snake) - 1].y
    return x, y


def game_over():
    """Handles player losing"""

    global is_alive
    is_alive = False
    player_input = screen.textinput(title="Game over!", prompt="Play again?").lower()
    print(player_input)

    if player_input == "yes" or player_input == "y":
        maingame()

    elif player_input == "no" or player_input == "n":
        return False

    else:
        game_over()


def is_game_over():
    play_again = True

    def snake_hit_self():
        for segment in snake:
            if snake.index(segment) != 0:
                if snake[0].x == segment.x and snake[0].y == segment.y:
                    game_over()

    def snake_hit_border():

        # Checks if snake head position is outside of border
        if snake[0].x >= screen.canvwidth / 2 or snake[0].x <= screen.canvwidth / -2 or snake[0].y >= screen.canvheight / 2 or snake[0].y <= screen.canvheight / -2:
            game_over()

    snake_hit_border()
    snake_hit_self()

    return play_again


def maingame():
    global snake
    global fruits
    global default_key

    screen.clear()
    screen.setup(height=1000, width=1000)
    screen.bgcolor("black")
    screen.tracer(0)
    screen.listen()

    # Key logger
    screen.onkey(lambda x="w": key_logger(x), key="w")
    screen.onkey(lambda x="a": key_logger(x), key="a")
    screen.onkey(lambda x="s": key_logger(x), key="s")
    screen.onkey(lambda x="d": key_logger(x), key="d")
    draw_border()

    default_key = "w"

    snake = [Segment(60, 0), Segment(40, 0), Segment(20, 0), Segment(0, 0)]
    fruits = [Fruit(0, 0)]
    for segment in snake:
        segment.create()
    fruits[0].create()
    fruits[0].move()
    fruits[0].generate_new_position(screen_width=screen.canvwidth, screen_height=screen.canvheight, snake=snake)

    is_alive = True

    while is_alive:
        # Delay before next step
        sleep(0.15)

        # Move head based on pressed key
        move_head(default_key)

        is_alive = is_game_over()

        snake_tail_x_position, snake_tail_y_position = snake_tail_position()

        # Check if a fruit was eaten
        eat_fruit(x_pos=snake_tail_x_position, y_pos=snake_tail_y_position)


maingame()
