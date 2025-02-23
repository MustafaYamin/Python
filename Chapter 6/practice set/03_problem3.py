p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

comment = input("Write a comment: ")

if((p1 in comment) or (p2 in comment) or (p3 in comment) or (p4 in comment)):
    print("This comment is a spam")

else:
    print("This comment is not a spam")

# Here we used in method it is used to identify if an item contains a specefic value in it