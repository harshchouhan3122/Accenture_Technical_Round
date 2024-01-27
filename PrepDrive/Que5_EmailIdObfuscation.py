'''
Question 5 : Email ID Obfuscation


Personal information like email id and other contact details need to be handled in a way so that privacy of the user is safeguarded. One way to do this is to hide or partially hide such information, also called obfusction the information.

Given the email id as input, the program should obfuscate the id as follows :

1) For the given mail id, the part that comes before @ is referred to as the first part. If there is no first @ character, the mail id is invalid.

2) If the first part of the email id is less than or equal to 5 characters in length, replace all characters in the first part with *

3) If the first of the email id is greater than 5 characters in length, print the first 3 characters as it is and replace the remaining characters of the first part with *



4) If the email id is invalid, print Invalid Input.


Example 1

Input :
abc@gmail.com

Output :
***@gmail.com

Explanation

Here the first part is 'abc'. This is less than 5 characters in length, so replace all characters in the first part with *.


Example 2

Input :
abcdefghi@gmail.com

Output :
abc******@gmail.com

Explanation

Here the first part is 'abcdefghi'. This is more than 5 characters in length, so replace all characters in the first part except the first with *.


Complete the function obfuscateMailId in the editor. The function must print the obfuscate mail id as per the rules mentioned. If the mail id is invalid, it should print Invalid Input. obfuscateMailId has the following parameter(s) :

mailid : a string representing the mail id


Constraints :
1) A valid mail id should contain the character @ ( e.g. myid_at_gmail is invalid)
2) A valid mail id should have first part with at least one or more characters ( e.g. @myid is invalid)
'''

def obfuscateMailId(email):
    def validMail(email):
        email = email.split("@")
        if email[-1] == "gmail.com" and (email[0].lower() >= 'a' and email[0].lower() <= 'z'):
            return True
        else:
            return False
        
    if validMail(email):
        req = "@gmail.com"
        email = email.split("@")
        name = email[0]
        if len(name) <= 5:
            data = "".join(["*"]*len(name))
        else:
            data = name[:3] + "".join(["*"]*(len(name)-3))

        return data+req

email1 = "abc@gmail.com"
email2 = "abcdefghi@gmail.com"

print(obfuscateMailId(email1))
print(obfuscateMailId(email2))