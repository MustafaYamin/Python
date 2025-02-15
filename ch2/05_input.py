# Input function is used to take input from the user in python
# It takes input in the form of string

# Taking input from the user
name = input("Enter your name: ")
print("Hello", name)

# But if you want to add 2 numbers then you have to convert the input to integer
# otherwise it will be treated as string and will be concatinated like below
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
sum = num1 + num2
print("Sum is: ", sum) # It will give the answer like 12 if the sum was of 1 and 2

# I you want to add 2 numbers then you have to convert the input to integer like below
value1 = input("Enter first number: ")
converted_value1 = int(value1)
value2 = input("Enter second number: ")
converted_value2 = int(value2)
sum = converted_value1 + converted_value2
print("Sum is: ", sum) # It will give the answer like 3 if the sum was of 1 and 2