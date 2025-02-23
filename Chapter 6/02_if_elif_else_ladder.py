# if elif else ladder

# Now lets see what is elif used for

# lets say we are making a program which checks the age and tells if a person is a minor or not
# But we want to make sure that the useres are not entering age like 0 or negative numbers

# Here we are asking user to enter age
a = int(input("Enter you age: "))

# Here we are saying that if the age entered by the user is 18 or more then print You are a major.
if(a>=18):
    print("You are a major.")

# elif runs when the condition in if is not matched 
# Here we are saying that if the age entered by the user is 0 or less then 0 print Please enter correct age.
elif(a<=0):
    print("Please enter correct age.")

# else runs when the condition in if and elif both are not matched 
# Here we are saying the if the condition of both if and elif are not matched print You are a minor.
else:
    print("You are a minor.")

