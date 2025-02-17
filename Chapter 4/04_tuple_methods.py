# Just like how string methods returns a new string or a copy of a string same goes with tuple it will never change the existing tuple 

a = (1, 1, "Mustafa", "Mustafa", False, 99.1)

# count method counts that how many times a value is in our tuple
no = a.count(1)
print(no) #Output: 2

# index method is used to find that on which index a value is placed in a tuple
# once it finds the value it does not matter if the same value is twice in the tuple it will not look further

i = a.index("Mustafa") #Output: 2
print(i)

# There are more methods like len() for tupel to check the length of the tuple but those are for you to explore 

# Note: Use AI tools like Chatgpt to thrive in the AI era and ask it as much questions as you can to learn fast