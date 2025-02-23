l = ["Mustafa", "Hakim", "Unzila", "Mosa","Wardah"]

searched_name = input("Search for a name: ")

if(searched_name in l):
    print(searched_name)
else:
    print("This name is not in records.")