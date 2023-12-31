# Slicing is a way to break a list into its components

string = ["R","A","A","A","H","!"]

# This will print every character between the two indexes (not including 5)
print(string[0:5])

# This will print all characters after index 1
print(string[1:])

# This will print all characters before index 4
print(string[:4])

string2 = [1,2,3,4,5,6,7,8,9,10]

# This will print all characters with an increment of 2
print(string2[::2])

# This will print the list backwards
print(string2[::-1])

# This also works for tuples
tuple1 = (1,2,3,4,5,6,7,8,9,10)

print(tuple1[0:5:2])