"""Shaining"""

# What is Chaining?
# Chaining is a technique that allows you to connect multiple operations or conditions together in a single line of code. This can make your code more concise, but it can also affect readability.

# Why use it?

# Readability: While chaining can make code shorter, it can also make it harder to understand, especially if the conditions are complex. Therefore, it is important to balance brevity with clarity.

# Usage: Use chaining when you have simple conditions and want to avoid multiple lines of code, but prefer more traditional decision structures when the logic is more complex.

x = 10

# Traditional decision structure
if x < 5:
    print("x is less than 5")
elif 5 <= x < 15:  # Chaining conditions
    print("x is between 5 and 15")
else:
    print("x is 15 or greater")

# Chaining with a ternary expression
result = (
    "x is less than 5"
    if x < 5
    else "x is between 5 and 15" if x < 15 else "x is 15 or greater"
)
print(result)
