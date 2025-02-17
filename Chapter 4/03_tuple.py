# Tuple is a collection of values and just like strings it is immutable
# A tuple is decleared using the following syntex

a = (1, "Mustafa", False, 99.1)

# Yes just like list tuple can also hold values of multiple data types

# If we print the type of a it will be shown as a tuple
print(type(a))

# lets make a tuple which holds only 1 value

b = (1)
print(type(b))
# Here it shows that b is of data type integer but we made a tuple!
# Python actually thinks that 1 is a number enclosed in round brackets so to make a 
# single value tuple we have to wite a comma after the value

c = (1,)
print(type(c))

# Reminder a tuple is always immutable