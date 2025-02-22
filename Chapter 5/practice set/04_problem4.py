s = set()
s.add(20)
s.add(20.0)
s.add("20")

print(f"s is {s} and length of s is {len(s)}")

# The length is 2 because the intiger 20 and and floating point number 20.0 are the same python will treet them as a same number
