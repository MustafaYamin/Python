# It sometimes get confusing for begginers to figure out the code when there are multiple if statements

# Lets say we have 2 if statements and both are taking the input from a

a = int(input("Enter you age: "))

# statement 1
# Here it is not connected with the if statement below it and it will run independently
if(a%2 == 0):
    print(f"{a} is an even number")

# This statement will end here

# statement 2
# This statement is not connected with the statement above and runs independently
if(a>=18):
    print("You are a major.")

elif(a<=0):
    print("Please enter correct age.")

else:
    print("You are a minor.")
# This statement will end here


# Here we understood that an if statement can be executed alone but an else and elif 
# can not work by them self they need an if statement