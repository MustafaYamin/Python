marks1 = int(input("Enter marks for subject 1: "))
marks2 = int(input("Enter marks for subject 2: "))
marks3 = int(input("Enter marks for subject 3: "))

# Check percentage

total_percentage = (100 * (marks1 + marks2 + marks3)) / 300

# check pass or fail

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You passed!", total_percentage)

else:
    print("You failed.", total_percentage)
