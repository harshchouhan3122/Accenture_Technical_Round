'''
Question:10 

Problem Statement 
A carry is a digit that is transferred to left if sum of digits exceeds
 9 while adding two numbers from 
right-to-left one digit at a time 
You are required to implement the following function. 
Int NumberOfCarries(int num1, int num2); 
The functions accepts two numbers ‘num1’ and ‘num?’ as its arguments. 
You are required to 
calculate and return the total number of carries generated while adding
 digits of two numbers 
‘num1’ and ‘ num?2'. 
Assumption: num1, num2>=0 
Example: 
e Input 
o Num 1: 451 
o Num 2: 349 
¢ Output 
o 2 
Explanation: 
Adding ‘num 1” and ‘num 2’ right-to-left results in 2 carries since 
( 1+9) is 10. 1 is carried and (5+4=1) 
is 10, again 1 is carried. Hence 2 is returned. 
Sample Input 
Num 1: 23 
Num 2: 563 
Sample Output 0
'''

# def carryCount(num1,num2):
#     carry = 0
#     count = 0
#     num1, num2 = list(str(num1)), list(str(num2))

#     # Converting both the numbers of equal length
#     if len(num1) < len(num2):
#         num1 = [0]*(len(num2)-len(num1)) + num1
#     else:
#         num2 = [0]*(len(num1)-len(num2)) + num2
#     # print(num1, num2)

#     # Reverse the number (Addition Starts from the Right to left)
#     num1, num2 = num1[::-1], num2[::-1]
#     print(num1, num2)

#     result = ""
#     digit = 0
#     for i in range(len(num1)):
#         sum = int(num1[i]) + int(num2[i]) + carry
#         print(f"sum={sum}, carry={carry}, digit={digit}, count={count}")
#         carry = 0
#         digit = sum
#         if sum >= 10:
#             count += 1
#             carry  = sum//10
#             digit = sum%10
#         result = str(digit) + str(result)
#         # result = int(result)
#         print(f"sum={sum}, carry={carry}, digit={digit}, count={count}, result={result}")
#         print("_________________________________________________________")
    # result = int(result)
    # print(f"{num3} + {num4} = {result}")
    # return (f"Carry Count = {count}")

def carryCount(num1,num2):
    num3,num4 = num1, num2
    carry, count= 0, 0
    num1, num2 = list(str(num1)), list(str(num2))

    # Converting both the numbers of equal length
    if len(num1) < len(num2):
        num1 = [0]*(len(num2)-len(num1)) + num1
    else:
        num2 = [0]*(len(num1)-len(num2)) + num2
    # print(num1, num2)

    # Reverse the number (Addition Starts from the Right to left)
    num1, num2 = num1[::-1], num2[::-1]

    result = ""
    digit = 0
    for i in range(len(num1)):
        sum = int(num1[i]) + int(num2[i]) + carry
        digit, carry = sum, 0
        if sum >= 10:
            count += 1
            carry  = sum//10
            digit = sum%10
        result = str(digit) + str(result)
    result = int(result)
    print(f"{num3} + {num4} = {result}")
    return (f"Carry Count = {count}")

# Inputs
num1, num2 = 451, 349
# Output : 2

num3, num4 = 13658, 2
# Output : 0

print(carryCount(num1, num2))
print(carryCount(num3, num4))