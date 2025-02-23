# Conditional Expresions

# Conditional expresions are used in such cases when we have a condition to check 
# lets say when the user enters an odd number we want to show you entered an odd number and
# when the user enters an even number we want to show you entered an even number

# We have 3 conditional expressions 
# if
# elif
# else

# Now lets say we want to check age to issue driving license 

# Here we are asking the user to enter his age
age = int(input("Enter your age: "))

# Here we are saying to python that if the age entered by the user is equal 
# to 18 or is greater then 18 then print you are eligible
# other wise python will automatically go to else and print you are not eligible
if(age>=18):
    print("You are eligible.")

else:
    print("You are not eligible.")

