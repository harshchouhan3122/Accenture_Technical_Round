'''
Question:11 
(Asked in Accenture Offcampus 1 Aug 2021, Slot 3) 
Problem Statement 
You are given a function, 
Void *ReplaceCharacter(Char str[], int n, char ch1, char ch2); 
The function accepts a string ‘ str’ of length n and two characters ‘ch1’ and ‘ch2’ as its arguments . 
Implement the function to modify and return the string * str’ in such a way that all occurrences of 
‘ch1” in original string are replaced by ‘ch2’ and all occurrences of ‘ch?’ in original string are replaced 
by ‘cht’. 
Assumption: String Contains only lower-case alphabetical letters. 
Note: 
¢ Return null if string is null. 
« If both characters are not present in string or both of them are same, then return the string 
unchanged. 
Example: 
¢ Input: 
o Str: apples 
o chla 
o ch2:p 
e Qutput: 
o paales 
Explanation: 
‘Ain original string is replaced with ‘p’ and ‘p' in original string is replaced with ‘a’, thus output is 
paales.
'''
def replaceChar(str1, ch1, ch2):
    str1 = list(str1)
    for i in range(len(str1)):
        if str1[i] == ch1:
            str1[i] = ch2
        elif str1[i] == ch2:
            str1[i] = ch1
    return "".join(str1)


# Input
str1, ch1, ch2 = "apples" , "a", "p"

# Output
print(replaceChar(str1,ch1,ch2))

