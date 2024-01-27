'''
Problem Description :
The Binary number system only uses two digits, 0 and 1 and number system can 
be called binary string. You are required to implement the following function:

int OperationsBinaryString(char* str);

The function accepts a string str as its argument. The string str consists 
of binary digit separated with an alphabet as follows:

 A denotes AND operation
 B denotes OR operation
 C denotes XOR Operation
You are required to calculate the result of the string str, scanning the string 
to right taking one opearation at a time, and return the same.

Note:

No order of priorities of operations is required
Length of str is odd
If str is NULL or None (in case of Python), return -1
Input:
str: 1C0C1C1A0B1

Output:
1

Explanation:
The alphabets in str when expanded becomes “1 XOR 0 XOR 1 XOR 1 AND 0 OR 1”, 
result of the expression becomes 1, hence 1 is returned.

Sample Input:
0C1A1B1C1C1B0A0

Output:
0'''


# def bitwiseOperations(str):
#     i = 1
#     length = len(str)-1

#     while(i<length):
#         result = ""

#         if str[i] == "A":
#             result = int(str[i-1]) & int(str[i+1])

#         elif str[i] == "B":
#             result = int(str[i-1]) | int(str[i+1])

#         elif str[i] == "C":
#             result = int(str[i-1]) ^ int(str[i+1])

#         else:
#             i += 1
#             continue

#         # str =  chr(result) + str[i:]
#         i += 1
#         length = len(str)-1
#         print(f"result = {result}, str = {str}")

#     return str


# def bitwiseOperations(str1):
#     str1 = list(str1)
#     i = 1
#     length = len(str1)-1
#     result = str1[0]

#     while(i<length):
#         print(f"str = {str1}")
#         result = ""

#         if str1[i] == "A":
#             result = int(str1[i-1]) & int(str1[i+1])
            

#         elif str1[i] == "B":
#             result = int(str1[i-1]) | int(str1[i+1])

#         elif str1[i] == "C":
#             result = int(str1[i-1]) ^ int(str1[i+1])

#         else:
#             i += 1
#             continue
        
#         str1.pop(0)
#         str1.pop(0)
#         str1.pop(0)
#         str1.insert(0,result)

#         print(f"result = {result}, str = {str1}")
#         print()

#         i = 0
#         length = len(str1)-1

#     return result


def bitwiseOperations(str1):
    str1 = list(str1)
    i = 1
    length = len(str1)-1
    result = str1[0]

    while(i<length):
        result = ""

        if str1[i] == "A":
            result = int(str1[i-1]) & int(str1[i+1])
            

        elif str1[i] == "B":
            result = int(str1[i-1]) | int(str1[i+1])

        elif str1[i] == "C":
            result = int(str1[i-1]) ^ int(str1[i+1])

        else:
            i += 1
            continue
        
        str1[i+1] = result
        # str1 = str1[3:]
        # str1.insert(0,result)
        # i = 0
        
        i += 1
        length = len(str1)-1

    return result


# Input
str1 = "1C0C1C1A0B1"
str2 = "0C1A1B1C1C1B0A0"

# Output
print(bitwiseOperations(str1))
print(bitwiseOperations(str2))