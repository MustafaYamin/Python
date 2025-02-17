# Just like we looked at stings functions there are many methods for lists but the difference 
# between string function and lists methods is that lists method when applied change the original lists
# unlike string where the orginal string was not changed

# lets look at the example of append method

# if I have a list of numbers and I want to add number 22 at the end of it I can simply use append method 
# append method does insertion at the end of our list meaning it will add the value given to it at the end of the list

num = [12, 343, 1, 987, 4, 44, 87]
num.append(22)
print(num)

# You might have noticed that we didn't created another variable to store the value returned by append method
# it is because it does not returns a new list instead it makes changes in our original string

# We have more methods like sort() it sorts a list of numbers in increasing 
# Note: uncomment and explore the methods once at a time otherwise you will face issues understanding

list = [1, 90, 67, 34, 87, 21, 100, 99, 101, 1000]
# list.sort() #uncomment to run
# print(list) #Output: [1, 21, 34, 67, 87, 90, 99, 100, 101, 1000]

# Similarly if we want to reverse our list we will use reverse method

# list.reverse()
# print(list) #output: [1000, 101, 99, 100, 21, 87, 34, 67, 90, 1]

# If we want to insert a number in the middle of our list or at our choosen index we 
# use insert method

# While using insert method we first give the index where we want to add our value and then after a comma we write our value

# list.insert(3, 3355) #here 3 is the index and 3355 is the value
# print(list) #Output: [1, 90, 67, 3355, 34, 87, 21, 100, 99, 101, 1000]

# Next we have pop method using which we can delete any value of our choice using it's index

# list.pop(4) #In our list 87 is at index 4 so it will be deleted
# print(list) #Output: [1, 90, 67, 34, 21, 100, 99, 101, 1000]

# There is an intresting thing about pop method that if we run it inside a print() statement it will print the value it is poping out

# print(list.pop(4)) #Output: 87

# There is also a remove method but it is a task for you to explore it

# You can always look for more list methods according to your use but here we have discussed the cumpolsery one
