CORRECT_EMAIL = "john.doe@gmail.com"
CORRECT_PASSWORD = "JD@789"

email = input("Enter Email: ")
password = input("Enter Password: ")

if email != CORRECT_EMAIL:
    print("Invalid Email")

elif password != CORRECT_PASSWORD:
    print("Incorrect Password")
    password = input("Enter Password Again: ")

    if password == CORRECT_PASSWORD:
        print("Logged In Successfully")
    else:
        print("Incorrect Password Again")

else:
    print("Logged In Successfully")
