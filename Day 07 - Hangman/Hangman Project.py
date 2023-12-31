import random
import string

word_list = ["word", "list", "lovely", "gold", "bee", "chess", "payment"]
chosen_word = word_list[random.randint(0, len(word_list) - 1)]
correct_letters = []
total_letters = []
letter_comparator = ""
chosen_letter = ""
unique_letters_in_word = []
life = 5
status = 0
# 0 = game in progress
# 1 = game won
# 2 = game lost

for letter in chosen_word:
    if letter not in unique_letters_in_word:
        unique_letters_in_word.append(letter)

def generate_spaces():
    # This function creates the spaces that show which letters have been found
    spaces = ""
    for letter in chosen_word:
        if chosen_letter == letter or letter in correct_letters:
            spaces += letter + " "
        else:
            spaces += "_ "
    return spaces


def letter_check():
    # This function checks if the inputted letter appears in the chosen word.
    # If it does, it will add the letter to the correct letters list, otherwise it will subtract a life.
    # The function also checks whether all the letters have been found in order to change the game's status
    global correct_letters
    global life
    global status
    index = 0
    score = 0

    if chosen_letter in chosen_word:
        correct_letters.append(chosen_letter)
    else:
        life -= 1
    if life == 0:
        status = 2
    # Checks to see if the letter is correct and subtracts a life if not

    for letter in correct_letters:
        if correct_letters[index] in unique_letters_in_word:
            score += 1
        index += 1
    # Checks if all the letters match the word

    if len(unique_letters_in_word) == score:
        status = 1
    # Changes the status to winning if all the letters match


print (generate_spaces())

# Main game loop. Breaks when status is either Losing or Winning.
while status == 0:
    chosen_letter = input("Choose a letter\n").lower()
    while len(chosen_letter) != 1:
        print("Choose *1* letter, dummy")
        chosen_letter = input("Choose a different letter:\n").lower()
        # Checks if only one character has been inputted.

    while chosen_letter in total_letters:
        print("Letter is already in list")
        chosen_letter = input("Choose a different letter:\n").lower()
        # This loop checks if the letter has already been submitted.

    while chosen_letter not in string.ascii_lowercase:
        print("That's not a letter you silly goose!")
        chosen_letter = input("Choose a different letter:\n").lower()
        # This loop checks if the inputted character is a letter.

    total_letters.append(chosen_letter)
    total_letters.sort()
    letter_check()
    generate_spaces()
    print(f"Lives: {life}\n{generate_spaces()}\n{total_letters}")

if status == 1:
    print("You won!")
else:
    print("You lost!")
