# Before diving into string splicing lets look at the concept of indexing in Python.
# Indexing and/or counting and/or numbering in Python starts from 0. 
# That means the first element in a list or string is at index 0.
# For Example:

name = "Mustafa"
# Here M is at index 0, u is at index 1, s is at index 2, t is at index 3, a is at index 4, f is at index 5, a is at index 6.

# We can also do reverse indexing in Python.
# Reverse indexing starts from -1. That means the last element in a list or string is at index -1.
# For Example:

name = "Mustafa"
# Here a is at index -1, f is at index -2, a is at index -3, t is at index -4, s is at index -5, u is at index -6, M is at index -7.

# Now lets look at string splicing in Python.
# By splicing a string we can slice it to get a part of it.

# Firstly lets see how to find the length of a string?
# lets say we have a string:
food = "Burger"
length_of_food = len(food) # len() is a built-in function in Python that returns the length of an object.
print(length_of_food) # Output: 6

# Now lets see how to slice a string in Python?
# The syntex to slice a string in Python is:
# string_name[start_index:end_index]
# For example:
city = "Chicago"
# This will slice the string from index 0 to index 3.
# meaning it will include from 0 "c" to 3 "c" but not include 4 "a".
shortCity = city[0:3] 
print(shortCity) # Output: Chi

# lets say we want to print character 1
character1 = city[1]
print(character1) # Output: h because h is at index 1.