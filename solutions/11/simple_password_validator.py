"""simple_password_validator"""

password = "1234"

attempts_remaining_before_blocking = 4

password_entered = ""

while attempts_remaining_before_blocking > 0:

    password_entered = str(input("Enter your password: "))

    if password_entered == "":
        while password_entered == "":
            print("sorry, input a valid password")
            password_entered = str(input("Enter your password: "))

    attempts_remaining_before_blocking -= 1

    if attempts_remaining_before_blocking <= 1 and password_entered != password:
        print("this is your last chance!")

    if password_entered != password:
        print("Sorry, wrong password!")
