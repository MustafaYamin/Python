l = [True, "Mustafa", 1.98, 67, 'Usman']

i = 0

while (i<len(l)):
    print(l[i])
    i += 1


# Now lets understand what happens here:
# we have a list l containing multiple values 
# we created a variable and made it's value 0

# In our while loop we said that while i is less then length of l (which is true because value of i is 0)
# print i in l which means it will print the 0 index of l (the 0 index contains the value True)
# Then we said to increment the value of i and as the value increments our loop will print the values at the 
# incremented index till len of l is no longer less then i and the while loop will end