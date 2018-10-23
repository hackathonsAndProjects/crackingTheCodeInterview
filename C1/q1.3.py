# CRACKING THE CODE INTERVIEW 
# CHAPTER 1: ARRAY INTERVIEW QUESTIONS 

""" URLify: Write a method to replace all spaces in a string
with '%20'. You may assume that the string has sufficient 
space at the end to hold the additional characters, and that 
you are given the "true" length of the string. 
(Note: If implementing in Java, please use a character array
 so that you can perform this operation in place.)
 """ 

 # PSEUDOCODE
 # procedure urlify:
 # prompt user for inputString and stringLength
 # initialize empty string, output = " " 
 # for position in range(stringLength+1)
        # if inputString[position] == " " and not at end of list
            # output += "%20"


def urlify():
    print("Please input the string and its length, x.")
    rawInput = input('Format: "Type your string here", X for string length: ').split(",")
    inputString = rawInput[0]
    stringLength = int(rawInput[1])
    print(rawInput)

    output = " "
    for pos in range(stringLength + 1):
       if (inputString[pos] == " "):
           output += "%20"
        

urlify()

        
        