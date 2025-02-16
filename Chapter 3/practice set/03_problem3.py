a = "I live at street  19."

print(a.find("  "))

# here we are using .find function it creates a sub string of the original 
# string and then returns it's index. It starts counting the index from 1 so
# in the variable I is at index 1 according to .find function

# Another example of .find:

b = "I live at street 19"

print(b.find("at")) # It will print the index where at is located "7"

# But what if the string does not hold the value which we are finding?

c = "I live at street 19"

print(c.find("22")) #It will give -1 as a result which means that 22 does not exist in the string