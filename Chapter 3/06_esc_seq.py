# Escape sequence characters are some special characters that are used to perform some specific tasks in python.

# here are some examples:
a = "I am a good boy but not a bad boy." 
print(a)
# output: I am a good boy but not a bad boy.

#If I want to print this string in multiple lines, I can use \n.

a = "I am a good boy\nbut not a bad boy." #Here \n is a escape sequence character.
print(a) 
#output:I am a good boy    
# but not a bad boy.

# lets say I want to give a tab space between the two lines, I can use \t.
a = "I am a good boy\n\tbut not a bad" #Here \t is a escape sequence character.   
print(a)
#output:
# I am a good boy    
#         but not a bad boy.

# Now lets see how to use single and double quotes in a string.
# if I want to highlight a word in a string and I am willing to keep it in doubble quotes, 
# I can not use double quotes directly.

# b = "This ting is called "This"" #This will give an error.
# print(b) #Output: SyntaxError: invalid syntax

# Instead I can write it like this: \"This\"

b = "This ting is called \"This\"" #This will not give an error.
print(b) #Output: This ting is called "This"

# There is how ever another way to do this. 
# You can use single quotes to highlight a word in a
#  string if you are using double quotes for the string and the same way around.
# Example:

b = 'This ting is called "This"' #This will not give an error.
print(b) #Output: This ting is called "This"
b = "This ting is called 'This'" #This will not give an error.
print(b) #Output: This ting is called 'This'

# If you want to literally use \ in a string, you can use \\.
# Example:
c = "and\\or" #Here \\ is a escape sequence character.
print(c) #Output: and\or

# You can always look for more escape sequence characters in the documentation
# or use chatgpt to look them for you according to your use.