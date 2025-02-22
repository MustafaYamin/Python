# 1st an approach
nums = input("Enter any 8 numbers: ")
uniqueNums = set(nums)
print(uniqueNums)

# 2nd approach
s = set()
n = input("Enter 1st number: ")
s.add(int(n))
n = input("Enter 2nd number: ")
s.add(int(n))
n = input("Enter 3rd number: ")
s.add(int(n))
n = input("Enter 4th number: ")
s.add(int(n))
n = input("Enter 5th number: ")
s.add(int(n))
n = input("Enter 6th number: ")
s.add(int(n))
n = input("Enter 7th number: ")
s.add(int(n))
n = input("Enter 8th number: ")
s.add(int(n))

print(s)

# It is for you to find whuch approach is better