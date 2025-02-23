num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

if(num1>num2 and num1>num3 and num1>num4):
    print(f"The greatest number is number 1: {num1}")

elif(num2>num1 and num2>num3 and num2>num4):
    print(f"The greatest number is number 2: {num2}")

elif(num3>num2 and num3>num1 and num3>num4):
    print(f"The greatest number is number 3: {num3}")

elif(num4>num2 and num4>num3 and num4>num1):
    print(f"The greatest number is number 4: {num4}")