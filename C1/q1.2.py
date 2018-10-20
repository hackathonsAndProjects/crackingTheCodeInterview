# CRACKING THE CODE INTERVIEW 
# CHAPTER 1: ARRAY INTERVIEW QUESTIONS 

""" 1.1 Check Permutation: Given two strings, write a method
to decide if one is a permutation of the other """

# First, we need to understand what a permutation is. 
# We need to determine if the strings contain the same 
# letters but in a different order. 

""" PSEUDOCODE 
We can have a counter variable that keeps track of the
number of similiar letters. in the end, compare with the 
length of the string.

Error Handling: 
    - Check if strings are the same length.
    - Handle upper and lower cases.
    - Handle duplicate letters

procedure isPermutation(str1, str2)
    permutation = False
    # Check strings are of equal length
    if (len(str1) != len(str2)): 
        return permutation 
    else: 
        sameLetter = 0
        for letter in str1:
            if (letter in str2):
                sameLetter += 1 
    
    if (sameLetter == len(str2)):
        return permutation = True
    else:
        # It's not a permutation, therefore false.
        return permutation
"""

# VERSION 1.2A
def isPermutation(str1, str2):
    permutation = False
    # Check strings are of equal length
    if (len(str1) != len(str2)): 
        return permutation 
    else: 
        sameLetter = []
        for letter in str1:
            if (letter not in sameLetter) and (letter in str2):
                sameLetter.append(letter)
            else:
                permutation = False
    
    if (len(sameLetter) == len(str2)):
        # If each letter in str1 is in str2
        permutation = True
   
    return permutation
    

# VERSION 1.2B: Ask for input strings and case sensitivity
def isPermutation2():
    print("Check if two strings are permutations of each other!")
    str1 = input("Input first string: ")
    str2 = input("Input second string: ")

    permutation = False
    # Check strings are of equal length
    if (len(str1) != len(str2)): 
        return permutation 
    
    # Keep asking until valid input is entered by the user
    # Anything other than Y(es) and N(o) is invalid.
    while True:
        caseSensitive = input("Do you want it case sensitive [Y/N]?: ")[0]
        if (caseSensitive.upper() == "Y"):
            break
        elif (caseSensitive.upper() == "N"):
            str1 = str1.upper()
            str2 = str2.upper()
            break


    # Set a counter to keep track of the same letters 
    # in both strings. 
    sameLetter = []
    for letter in str1:
        if (letter not in sameLetter) and (letter in str2):
            sameLetter.append(letter)
        else:
            permutation = False
    
    if (len(sameLetter) == len(str2)):
        # If each letter in str1 is in str2
        permutation = True
   
    return permutation
    
