"""Decision structures"""

# Example code with decision structures

# Asks the user to enter a number
number = int(input("Enter a number: "))

# Checks if the number is positive, negative, or zero
if number > 1:
    print("The number is positive.")

    # Checks if the number is even or odd
    if number % 2 == 0:
        print("And it is also even.")
    else:
        print("And it is also odd.")

elif number < 0:
    print("The number is negative.")

    # Checks if the negative number is even or odd
    if number % 2 == 0:
        print("And it is also even.")
    else:
        print("And it is also odd.")

else:
    print("The number is zero.")

# If ternary
age = 20
print("ok") if age >= 18 else print("sorry")
