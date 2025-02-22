# Dictionary in python is a key value pair which is used to store data. 
# You can also understan it by asuming it as a list of key value pairs.

# The syntex for making a dictionary is:

marks = {
    "Mustafa" : 100,  #Here Mustafa is the key and 100 is the value
    "Hakim" : 90,
    "Ibrahim" : 94,
}

# lets first check the type of marks and also print it

print(type(marks), marks) #Output: <class 'dict'> {'Mustafa': 100, 'Hakim': 90, 'Ibrahim': 94}

# Now what if we want to extract a specific value like we did in list

# print(marks[0]) #This will give error because you can not extract a value using index in dictionary.


# To extract any specific value from dictionary the key itself is used. 

# But the question is why?

# Well lets assume we are making results of students and there are 1000 students 
# and we have stored the marks in a list so in order to make every result we must know on which index is that specific student
# which would be very difficult. 

# In these type of situations we use dictionary

# Example: 
print(marks["Mustafa"]) #Output: 100 

# There are some properties of dictionary 
# 1: It is unordered
# 2: It is mutable
# 3: It is indexed
# 4: It can not contain duplicate or same keys.