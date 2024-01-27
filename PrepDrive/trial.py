def validMail(email):
    email = email.split("@")
    if email[-1] == "gmail.com" and (email[0].lower() >= 'a' and email[0].lower() <= 'z'):
        print("Valid")
    else:
        print("Not Valid")
    return email


email = "absc@gmail.com"
email = "absc@gmail.com2"
email = "@gmail.com"
email = "23a@gmail.com"
email = "A23@gmail.com"

print(validMail(email))