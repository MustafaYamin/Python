# Negative slicing in Python is used to slice a string from the end of the string.
# The syntax for negative slicing is:
# string_name[negative_start_index:negative_end_index]
# For example:
city = "Chicago"
shortCity1 = city[-4:-1] # This will slice the string from index -4 to index -1.
print(shortCity1) # Output: cag

# Trick: if you want to figure out the result of negative slicing you can alway convert it to
#  positive slicing and then figure out the result.


# what if you are asked what is:
print(city[:4]) #this means you are asked the answer of print(city[0:4]) which is "Chic"
print(city[2:]) #this means you are asked the answer of print(city[2:6]) which is "icago"
print(city[:]) #this means you are asked the answer of print(city[0:6]) which is "Chicago"

# Negative slicing can also be used to reverse a string.
# For example:
city = "Chicago"
reverseCity = city[::-1] # This will reverse the string.
print(reverseCity) # Output: ogacihC


# Negative indexing is most unlikely to be used in practicle scenarios but it is good to know about it to crack interviews.

