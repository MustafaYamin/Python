# Dictionary methods

marks = {
    "Mustafa" : 100,  
    "Hakim" : 90,
    "Ibrahim" : 94,
}

# .items is a method which gives us the items in a dictionary in a tuple form
print(marks.items()) 

# .keys gives us only the keys of the values in a tuple form
print(marks.keys())

# .values gives us only the values from the key value pair and also shows them in a tuple form
print(marks.values())

# We can update uor dictionary using update method and it will change our original dictionary because dictionary is mutable
marks.update({"Mustafa" : 99, "Tahira" : 87})
print(f"updated marks are: {marks}")
# update method updates the value currently present in the dictionary and adds the values which were not previously in the dictionary

# .get method is used to get the value of a specefic key
print(marks.get("Mustafa"))
# Now what if I am accessing a key which does not exist in the dictionary
print(marks.get("banana")) #It will print None

# Here a question arrives we previously saw that we can get the value of a specefic key 
# using square brackets then what is the difference in using .get method 
# lets see using the example

# If I want to get a value which does not exist in the dictionary
print(marks.get("apple")) #This will print None
# Where
# print(marks["apple"]) #This will return Key Error

# We can also print the length of a dictionary
print(len(marks))