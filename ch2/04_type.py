# type is a built-in function in Python that returns the type of the object.

a = 5
type(a) # <class 'int'>
print("type of a is: ",type(a))

b = 5.0
type(b) # <class 'float'>
print("type of b is: ",type(b))

c = 'Hello'
type(c) # <class 'str'>
print("type of c is: ",type(c))

d = True
type(d) # <class 'bool'>
print("type of d is: ",type(d))


# Type conversion
# You can convert one type to another using the int(), float(), and str() methods.

age1 = 25
print("type of age1 is:",type(age1))
changedType1 = str(age1) # '25' it is a string now
print("changed type of age1 is:",type(changedType1))

age2 = '25'
print("type of age2 is:",type(age2))
changedType2 = int(age2) # 25 it is an integer now
print("changed type of age2 is:",type(changedType2))

age3 = '25'
print("type of age3 is:",type(age3))
changedType3 = float(age3) # 25.0 it is a float now
print("changed type of age3 is:",type(changedType3))