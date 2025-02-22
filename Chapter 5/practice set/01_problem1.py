words = {
    "madad" : "Help",
    "paani" : "Water",
    "khirki" : "Window",
    "chamach" : "Spoon"
}

searchedWord = input("Search for translation: ")

print(f"{searchedWord} means: {words.get(searchedWord)}")