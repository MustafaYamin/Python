marks = int(input("Enter marks to check grade: "))

if((marks>=90) and (marks<=100)):
    grade = "Ex"
elif((marks>=80) and (marks<=89)):
    grade = "A"
elif((marks>=70) and (marks<=79)):
    grade = "B"
elif((marks>=60) and (marks<=69)):
    grade = "C"
elif((marks>=50) and (marks<=59)):
    grade = "D"
elif((marks<50)):
    grade = "F"
else:
    print("invalid marks entered")

print("Your grade is: ", grade)