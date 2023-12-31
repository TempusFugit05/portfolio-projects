# TODO:
#   1. Create Password Generator X
#   2. Create Password Storage System X
#   3. Make GUI x
#   4. Make Automatic Password Copying Functionality x

from random import randint, shuffle
import tkinter
from tkinter import messagebox
import string
import pandas

# This library allows for the copying of text to the clipboard
import pyperclip

# All characters that can be used to generate a password
PASSWORD_CHARS = ([char for char in string.ascii_letters] +
                  [char for char in string.digits] +
                  [char for char in string.punctuation])
PASSWORD_CHARS.remove(",")

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


def add_password(website, username, password):
    """Add password to file"""
    file = pandas.read_csv("passwords")

    # Read data and convert to dataframe
    data = pandas.DataFrame(file, columns=["website", "username", "password"])

    # Add new password to dataframe
    data = data._append({"website": website, "username": username,
                        "password": password}, ignore_index=True)

    # Save to file
    data.to_csv("passwords")


def reset_all_passwords():
    """RESETS ALL PASSWORD DATA"""
    with open("passwords", "w") as file:
        file.write("website,username,password")


def check_inputs():
    """Gets user input, checks for errors and saves"""
    # Get all necessary data and do initial processing
    website = website_input.get().strip().lower()
    username = username_input.get().strip()
    password = password_input.get().strip()

    # Checks for potential problems
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        error_label.config(text="ERROR: ALL FIELDS MUST BE FULL")

    elif "," in website or "," in username or "," in password:
        error_label.config(text="ERROR: FIELDS SHOULD NOT INCLUDE COMMAS")

    # If checks pass, save password
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
            add_password(website=website, username=username, password=password)
            pyperclip.copy(password)

            # Delete all fields
            password_input.delete(0, "end")
            username_input.delete(0, "end")
            website_input.delete(0, "end")


# Defining widgets
# Define window
root = tkinter.Tk()
root.minsize(width=500, height=500)
root.config(padx=50, pady=50)

# Website related widgets
website_label = tkinter.Label(text="Website: ", font=DEFAULT_FONT, padx=DEFAULT_PADX, pady=DEFAULT_PADY)
website_label.grid(row=1, column=0)

# Note: It's possible to get a widget to span over multiple columns using the columnspan attribute
website_input = tkinter.Entry(font=DEFAULT_FONT, width=50)
website_input.grid(row=1, column=1, columnspan=2)

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
