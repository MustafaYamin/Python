# List

# List is a container to store multiple values of any data type

a = ["Apple", "Orange", 5, 0.89, False]
# You might have noticed that our list contains values of different data types

print(a) #Output: ["Apple", "Orange", 5, 0.89, False]

# Now lets say that I want to extract Orange from the list I can do it using the index 
# (Yes a list is also indexed and also starts with 0)
#  of of orange in the list which is 1

print(a[1])

# If you remember I told you that strings are immutable so we can't change things in an existing string
name = "Mustafa"
# name[0] = "T"
# print(name)  This will give error of item assignment because we can not make changes in a string

# But we can make changes in a list
# lets make a new list
fruits = ["Apple", "Mango", "Orange", "Banana"]
# Lets change Apple and make it Pineapple
fruits[0] = "Pineapple" 
print(fruits[0])

# This means that lists are mutable unlike strings

# We can also do splicing in lists just like strings
# Example:
countries = ["Pakistan", "USA", "Russia", "India", "China"]
# If I want to access USA and Russia I can splice them using their indexes like below 

print(countries[1:3])
