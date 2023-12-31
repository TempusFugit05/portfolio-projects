# When trying to deal with errors that may arouse during code execution, it is useful to have a method of catching
# them without halting the program altogether

# Using the try keyword we can try and execute a piece of code and react accordingly whether it fails or not
try:
    file = open("test_file.txt")

# Using the except keyword we can specify what happens when an error has occurred
# The problem with this though, is that the exception will get triggered regardless of the error that arouse
except:
    print("The file was not found\nCreating a new file...")
    file = open("test_file.txt", "w")
    file.write("Success!")

# We can also specify what will happen if our try attempt is successful
else:
    print(file.read())

# The finally statement will execute regardless of the outcome
finally:
    file.close()


"""# Instead, we could specify on what occasion the exception will occur
try:
    test_list = [1, 2, 3, 4]
    print(test_list[4])
    file = open("test_file.txt")

except FileExistsError:
    print("file not found")

except IndexError as error_message:
    print(f"index out of range")

    # We can specify our own error messages using the raise statement which will print out the error type
    # along with an optional custom message
    raise IndexError("YOUR INDEX IS OUT OF RANGE DUMMY!")

"""

# A more realistic example of why these keywords are necessary would be something with an input
# Let's create a BMI calculator for example

weight = float(input("weight"))
height = float(input("height"))

if height >= 3:
    raise ValueError(f"NO WAY YOU'RE {height}m TALL")
bmi = weight/height**2
print(bmi)