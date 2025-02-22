# Union in sets

# union basically means to write the values from 2 sets and do not repeat the values which are repeated or are same

# Example:
s1 = {1, 32, 45}
s2 = {45, 19, 33}

print(s1.union(s2)) #Output: {32, 1, 33, 19, 45} 

# In the output we can see it did not printed 45 twice and returned a set of all values from both sets

# Intersection in sets

# Intersection means to print only the common values from both sets

print(s1.intersection(s2)) #Output: {45}
