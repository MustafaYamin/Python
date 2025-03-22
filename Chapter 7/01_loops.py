# Loops

# Loops in any programming lanuage are used to perform repetitive tasks without repeating the code

# lets say I want to write numbers 1-100 it will be very dificult to write
print("Manually writen")
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)

# This will be very dificult

# So rather then doing the task like this we use loops

print("Loop")
for i in range (1, 101):
    print(i)

# Now lets understand the above code
''' 
Here I have made a for loop which says that:
for i (here i is a variable) run the range function (which is a function of python and is used to determine the range of 
something) and the range will start from 1 and end 101 (we are writing 101 because the last value of the is not printed so 
in order to print 100 we are giving the range til 101) and now print the value of i

We will discuss how does it works but for no remember in python we have 2 types of loops
while loop
for loop


'''