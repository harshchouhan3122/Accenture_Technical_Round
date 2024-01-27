def replaceCharacters(string1,char1,char2):
    string1 = string1.replace(char1,char2.upper())
    string1 = string1.replace(char2,char1.upper())
    return string1.lower()

# Input
# str1 = input()
# char1 = input()
# char2 = input()

str = "apples" 
ch1 = "a" 
ch2 = "p" 

# Output
# print(replaceCharacters(str1,char1,char2))
print(replaceCharacters(str,ch1,ch2))
# paales 