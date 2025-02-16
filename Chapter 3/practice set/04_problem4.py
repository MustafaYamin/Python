a = "I live at street  19."

# here we are using .replace function again to replace double spaces with single space 
print(a.replace("  "," ")) 

# Reminder: Strings are immutable meaning the original string can not be changed 
# and it can be said that all the functions run on a copy of the string so
# if we print a it will give us the original string

print(a)