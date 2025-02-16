# Skip value in a string is used to skip a certain number of characters while slicing a string.
# This means that you can skip a certain number of characters while slicing a string.
# For example:

count = "0123456789"
skipValue = count[1:7:3] 
# We will first resolve [1:7] which is 123456 and then we will skip 3 characters which will give us 14.
# meaning it will skip the characters at index 2, 5.
print(skipValue) # Output: 14

# This means that after solving [1:7] it selected characters 123456 as they were on the index 1 to 7 then 
# to resolve the :3 it skipped 3 characters and selected 14 as they were on the index 1 and 4.

# lets see another example:

b = 'abcdefghijklmnopqrstuvwxyz'
c = b[1:9:4]
print(c) # Output: bf

# How does the above example work?
# we will first resolve [1:9] which is bcdefghi
# then will skip 4 characters from the resolved [1:9] 
# meaning it will first pick b and then skip 4 characters and pick f and then 
# there will be no character left to pick.

# I we look into it in detail:
b = 'abcdefghijklmnopqrstuvwxyz'
c = b[1:9]
print(c) # Output: bcdefghi

e = c[::4]
print(e) # Output: bf