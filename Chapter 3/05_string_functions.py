# There are many functions that can be used with strings. Here are some of them.

# To find the length of a string, use the len() function.
# It will also include the spaces in the length.
name = "Mustafa Yamin"
print(len(name)) # Output: 13 

# endsWith() function is used to check if a string ends with a specific character or not.
# It returns a boolean value.(True or False)
name = "Mustafa"
print(name.endswith("fa")) # Output: True
print(name.endswith("fay")) # Output: False

# What if I write:
print(name.endswith("A")) # Output: False
# This means that this function is case sensitive.

# Similarly, we have a function called startsWith() 
# which is used to check if a string starts with a specific character or not.
city = "Karachi"
print(city.startswith("Kar")) # Output: True
print(city.startswith("kar")) # Output: False
print(city.startswith("Ker")) # Output: False
# This means this function is also case sensitive.


# capatalize() function is used to capitalize the first character of a string.(It will not capatalize the whole string)
name = "mustafa"
print(name.capitalize()) # Output: Mustafa

# There are many functions for strings. You can find them in the documentation 
# and can also use Chatgpt to find them usng the promp below.
# Give me most used string functions in python.

# Note: There is no need to remember all the functions. You can always find them in the documentation.