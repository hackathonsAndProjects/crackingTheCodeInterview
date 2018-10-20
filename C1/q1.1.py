# CRACKING THE CODE INTERVIEW 
# CHAPTER 1: ARRAY INTERVIEW QUESTIONS 

""" 1.1 Implement an algorithm to determine if a string 
 has all unique characters. What if you cannot use additional
 data structures? """

 # First, let's go with our instinct and try to solve this 
 # using a data structure then get rid of it.

# VERSION 1.1A
def isUnique(inputStr):
    unique = True 
    characters = []
    for letter in inputStr:
        if (letter not in characters):
            # Append each new letter that is encountered 
            # in the string.
            characters.append(letter)
        else:
            # Otherwise, exit the loop and return False. 
            unique = False
            break
    return unique

# VERSION 1.1B: WITHOUT THE DATA STRUCTURES
def isUniqueStr(inputStr):
    # Implement the same thing but with an additional string
    unique = True
    characters = " "
    for letter in inputStr:
        if (letter not in characters):
            characters += letter
        else:
            unique = False
            break
    return unique

