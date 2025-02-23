user_name = input("Enter user name here: ")

if(len(user_name)>10):
    print(f"User name: {user_name} contains more then 10 letters. Please make it short.")
elif(len(user_name)<10):
    print(f"User name: {user_name} should contain 10 letters. Please prolong it.")
else:
    print("Valid user name.")