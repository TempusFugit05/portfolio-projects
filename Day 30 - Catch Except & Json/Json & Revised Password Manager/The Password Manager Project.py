# TODO:
#   1. Create Password Generator X
#   2. Create Password Storage System X
#   3. Make GUI x
#   4. Make Automatic Password Copying Functionality x

from random import randint, shuffle
import tkinter
from tkinter import messagebox
import string
import json

# This library allows for the copying of text to the clipboard
import pyperclip

# All characters that can be used to generate a password
PASSWORD_CHARS = ([char for char in string.ascii_letters] +
                  [char for char in string.digits] +
                  [char for char in string.punctuation])

# Remove all forbidden character from allowed list
FORBIDDEN_CHARS = ["{", "}", '"']
for char in PASSWORD_CHARS:
    if char in FORBIDDEN_CHARS:
        PASSWORD_CHARS.remove(char)

# Some default values
DEFAULT_PASSWORD_LENGTH = 16
DEFAULT_PADX = 10
DEFAULT_PADY = 10
DEFAULT_FONT = ("NEW YORK", 12,)


def generate_password():
    """Generates password"""
    global PASSWORD_CHARS, DEFAULT_PASSWORD_LENGTH
    password = ""

    for i in range(DEFAULT_PASSWORD_LENGTH + 1):
        # Add to password a random character
        password += PASSWORD_CHARS[randint(0, len(PASSWORD_CHARS) - 1)]

    # Shuffling characters
    shuffle(list(password))

    # Converting to string
    "".join(password)
    return password


def display_password():
    """Displays generated password"""

    # Generating password and converting it to a stringvar object that tkinter can work with
    password = tkinter.StringVar(value=generate_password())

    # Display password
    password_input.config(textvariable=password)


def save_password(website, username, password):
    login_data = {
            website: {
                "username": username,
                "password": password,
            }
    }

    try:
        # Opening file for reading
        with open("passwords", "r") as file:

            # Loading the data inside the passwords file
            data = json.load(file)

            # Saving the existing data to update it
            data.update(login_data)

    except (json.JSONDecodeError, FileNotFoundError):
        reset_all_passwords()
        save_password(website=website, username=username, password=password)

    else:
        # Open file for writing
        with open("passwords", "w") as file:
            # Saving the data in a readable way
            json.dump(data, file, indent=4)



def reset_all_passwords():
    """RESETS ALL PASSWORD DATA"""
    with open("passwords", "w") as file:
        file.write("{\n\n}")


def check_for_invalid_chars(input_string):
    for char in input_string:
        if char in FORBIDDEN_CHARS:
            return True

    return False


def check_inputs():
    """Gets user input, checks for errors and saves"""
    # Get all necessary data and do initial processing
    website = website_input.get().strip().lower()
    username = username_input.get().strip()
    password = password_input.get().strip()

    # Checks for potential problems
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        error_label.config(text="ERROR: ALL FIELDS MUST BE FULL")

    elif check_for_invalid_chars(website) or check_for_invalid_chars(username) or check_for_invalid_chars(password):
        error_label.config(text=f"ERROR: THE CHARACTERS '{"".join(FORBIDDEN_CHARS)}' ARE NOT ALLOWED")

    else:
        error_label.config(text="")

        # Create popup dialog to ask for consent to save password
        confirm = messagebox.askokcancel(title="Confirm Password?",
                                         message=f"Your data will be saved as:"
                                         f"\n\nWEBSITE URL: {website}"
                                         f"\nUSERNAME: {username}"
                                         f"\nPASSWORD: {password}")
        # Save password if there is confirmation
        if confirm:
            # Add password to file
            save_password(website=website, username=username, password=password)
            pyperclip.copy(password)

            # Delete all fields
            password_input.delete(0, "end")
            username_input.delete(0, "end")
            website_input.delete(0, "end")


def search_password():
    website = website_input.get().strip().lower()
    try:
        with open("passwords", "r") as file:
            data = json.load(file)
            user_data = data[website]

    except FileNotFoundError:
        error_label.config(text="ERROR: FILE DOES NOT EXIST\n"
                                "ENTER YOUR FIRST PASSWORD TO GENERATE FILE")

    except KeyError:
        error_label.config(text="ERROR: PASSWORD NOT FOUND")

    else:
        messagebox.showinfo(title=f"Your password for {website}",
                            message=f"Your password is: {user_data["password"]}\n"
                                    f"Your username is: {user_data["username"]}")


# Defining widgets
# Define window
root = tkinter.Tk()
root.minsize(width=500, height=500)
root.config(padx=50, pady=50)

# Website related widgets
website_label = tkinter.Label(text="Website: ", font=DEFAULT_FONT, padx=DEFAULT_PADX, pady=DEFAULT_PADY)
website_label.grid(row=1, column=0)

# Note: It's possible to get a widget to span over multiple columns using the columnspan attribute
website_input = tkinter.Entry(font=DEFAULT_FONT, width=31)
website_input.grid(row=1, column=1)

# Button to search for existing data
website_search_button = tkinter.Button(text="Search", font=DEFAULT_FONT, command=search_password)
website_search_button.grid(row=1, column=2, sticky="w")


# Username related widgets
username_label = tkinter.Label(text="Username: ", font=DEFAULT_FONT, padx=DEFAULT_PADX, pady=DEFAULT_PADY)
username_label.grid(row=2, column=0)

username_input = tkinter.Entry(font=DEFAULT_FONT, width=50)
username_input.grid(row=2, column=1, columnspan=2)

# Password related widgets
password_label = tkinter.Label(text="Password", font=DEFAULT_FONT, padx=DEFAULT_PADX, pady=DEFAULT_PADY)
password_label.grid(row=3, column=0)

password_input = tkinter.Entry(font=DEFAULT_FONT, width=31)
password_input.grid(row=3, column=1, sticky="W")

generate_password_button = tkinter.Button(text="Generate Password", font=DEFAULT_FONT, command=display_password)
generate_password_button.grid(row=3, column=2)


save_button = tkinter.Button(text="SAVE", font=DEFAULT_FONT, width=35, command=check_inputs)
save_button.grid(row=4, column=1, columnspan=2)

error_label = tkinter.Label(text="", font=DEFAULT_FONT, fg="RED")
error_label.grid(row=5, column=1)

root.mainloop()
