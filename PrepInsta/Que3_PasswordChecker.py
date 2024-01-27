'''
Question 3: Password Checker
(Asked in Accenture OnCampus 10 Aug 2021, Slot 3)

You are given a function.
int CheckPassword(char str[], int n);
The function accepts string str of size n as an argument. Implement the function which returns 1 if given string str is valid password else 0.
str is a valid password if it satisfies the below conditions.

– At least 4 characters
– At least one numeric digit
– At Least one Capital Letter
– Must not have space or slash (/)
– Starting character must not be a number
Assumption:
Input string will not be empty.

Example:

Input 1:
aA1_67
Input 2:
a987 abC012

Output 1:
1
Output 2:
0
'''
def passwordChecker(password):

    length = len(password)
    if length < 4 or password[0].isdigit():
        return 0

    count_numeric = 0
    count_upper = 0
    # print(ord("A"), ord("Z"))
    for i in password:
        if i == "/" or i == " ":
            return 0

        elif i.isdigit():
            count_numeric += 1
        elif ord(i) >= 65 or ord(i) <=90:
            count_upper += 1
    
    if count_numeric>=1 and count_upper >=1 :
        return 1
    return 0

# Inputs
password1 = "aA1_67"
password2 = "a987 abC012"
password3 = "5a987bC012"
# Output 1: 1
# Output 2: 0

# Outputs
# print(int('1'))
print(passwordChecker(password1))
print(passwordChecker(password2))
print(passwordChecker(password3))