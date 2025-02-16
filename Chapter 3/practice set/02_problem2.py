# name thkes the name of user as input
name = input("Enter your name:")
# date takes the current date from the user
date = input("Enter date:")

letter = '''
        Dare <|Name|>,
            You are selected!
            <|Date|>
'''
# Prints the desired output and uses replace function 
# to replace <|Name|> and then from the string "in which name is changed" it changes the 
# <|Date|> from the user enterd name and date

# This replacing of something from which already something have beed changed is called chaining

print(letter.replace("<|Name|>",name).replace("<|Date|>",date))