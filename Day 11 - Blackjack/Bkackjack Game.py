# The goal of the game is to get as close to 21 with your cards without going over it.
# Going over 21 is called a bust, and it's game over
# All cards from 2 - 10 are counted as their face value
# Jack, Queen and King are all counted as having a value of 10
# Ace can either be 1 or 11 and is calculated to be the best outcome for the player
# The dealer gets 2 cards and shows the player one of them
# If the total of both sides is equal, they draw
# If the dealer gets 16 or less, he has to take another card
import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]*4


modified_dealer_hand = []


def choose_card():
    global cards
    chosen_card = cards[random.randint(0, len(cards)-1)]
    cards.remove(chosen_card)
    return chosen_card


def maingame():
    player_hand = [choose_card(), choose_card()]
    dealer_hand = [choose_card(), choose_card()]
    player_score = calculate_score(player_hand)
    global modified_dealer_hand
    add_card = "y"
    print(f"Your hand is {player_hand} With a score of {player_score}\nDealer's hand is {dealer_hand[0]}\n")
    while add_card == "y" and player_score < 22:
        add_card = input("Add another card?\n").lower()
        if add_card == "y" or add_card == "yes":
            player_hand.append(choose_card())
            player_score = calculate_score(player_hand)
            print(f"Your hand is {player_hand} With a score of {player_score}\nDealer's hand is {dealer_hand[0]}\n")
    winner = calculate_winner(player_hand=player_hand, dealer_hand=dealer_hand)
    dealer_score = calculate_score(dealer_hand)
    print(f"Your hand is {player_hand} With a score of {player_score}\nDealer's hand is {modified_dealer_hand} with a score of {dealer_score}\n")
    if winner == 0:
        print("It's a tie!")
    elif winner == 1:
        print("You win!")
    else:
        print("You lost!")
    play_again = input("Play again?\n").lower()
    global cards
    if play_again == "yes" or play_again == "y":
        cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]*4
        maingame()


def calculate_score(hand):
    score = 0
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            score += 10
        elif type(card) == type(1):
            score += card
        else:
            if score+11 <= 21:
                score += 11
            else:
                score += 1
    return score


def calculate_winner(player_hand, dealer_hand):
    winner = 0
    # 0 - Tie
    # 1 - Player won
    # 2 - Dealer won
    global modified_dealer_hand
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)
    while dealer_score < 17:
        dealer_hand.append(choose_card())
        dealer_score = calculate_score(dealer_hand)
    if player_score == dealer_score < 22:
        winner = 0
    elif dealer_score < player_score <= 21 or dealer_score > 21:
        winner = 1
    else:
        winner = 2
    modified_dealer_hand = dealer_hand
    return winner


maingame()
print("Goodbye!")
