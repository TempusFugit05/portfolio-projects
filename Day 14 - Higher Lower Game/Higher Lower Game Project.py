import random
from game_data import data
# Imports account data to be used in game

acc_data = data

def choose_account():
    """
    Chooses account at random from the account list.\n
    Also removes it from the list.
    :return:
    """
    global acc_data
    acc = acc_data[random.randint(0, len(acc_data) - 1)]
    acc_data.remove(acc)
    # Assigns a random account library to two variables.
    return acc


def check_answer(user_choice, score, acc1, acc2):
    """
    Compares accounts based on chosen accounts and determines if player was correct
    :param user_choice:
    :param score:
    :param acc1:
    :param acc2:
    :return:
    """
    is_game_over = False
    # Defines game over variable in this function

    if user_choice == "a":
        if acc1['follower_count'] > acc2['follower_count']:
            score += 1
            print(f"Correct!\nYour score is {score}")
        else:
            is_game_over = True
            game_over(score)
    elif user_choice == "b":
        if acc1['follower_count'] > acc2['follower_count']:
            score += 1
            print(f"Correct!\nYour score is {score}")
        else:
            is_game_over = True
            game_over(score)
    return score, is_game_over


def game_over(score):
    """
    Gets called when player loses.\n
    Resets game or ends program.
    :return:
    """
    print(f"Game over!\nYour final score is {score}")
    play_again = input("Play again?\n").lower()
    # Asks to play again

    while play_again != "yes" and play_again != "y" and play_again != "no" and play_again != "n":
        print("Not a valid input!")
        play_again = input("Play again?\n").lower()
        # Checks for a valid input

    if play_again == "yes" or play_again == "y":
        maingame()
    else:
        print("Goodbye!")
    # Resets or ends game depending on input


def maingame():

    global acc_data
    acc_data = data

    score = 0
    #Defines/Resets score

    is_game_over = False
    # Defines game over statement

    acc1 = choose_account()
    acc2 = choose_account()

    while not is_game_over:
        # Main game loop, breaks when player chooses to quit

        acc1 = acc2
        acc2 = choose_account()

        print(f"{acc1["name"]} is a {acc1["description"].lower()} from {acc1["country"]}\nVS\n"
              f"{acc2["name"]} is a {acc2["description"].lower()} from {acc2["country"]}")
        # Prints account info

        user_choice = input("choose A or B\n").lower()
        # Asks user to guess which account has a higher follower count

        while user_choice != "a" and user_choice != "b":
            print("That's not a valid input!")
            user_choice = input("choose A or B\n").lower()
            # Test for correct input

        score, is_game_over = check_answer(user_choice=user_choice, score=score, acc1=acc1, acc2=acc2)
        # Checks if player was correct


maingame()