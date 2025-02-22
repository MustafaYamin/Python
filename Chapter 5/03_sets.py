# Sets

# Sets is also used to store a collection of data and it's syntex is:
s = {1, 36, 98, 4}
print(s) #You mignt notice that the output for s does not maitain it's order so if we want to maintain order we have to use list

# Then why use sets?

# In a set a value can not be repeated 
# eg:
e = {32, 32, 45, 5 , 6, 4, 4, 4}
print(e) # So you see it will not include the repeated values

# Now lets see how to make an empty set (Asked in interviews)
# If we write something like:
a = {} #This is an empty dictionary
print(type(a))

# to make an empty set we write
b = set() #This is an empty set
print(type(b))

# There can be other data types in sets
c = {"Mustafa", 9, 78, True, 0.65} #This is valid
print(c, type(c))

# Properties of sets:

# 1: Sets are unordered like we saw earlier
# 2: Sets are unindexed meaning you can not access a value using index
# 3: You can not change items form a set (But you can delete a value and add another value)
# 4: Sets can not contain repeated values