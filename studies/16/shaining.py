"""Shaining"""

# What is Chaining?
# Chaining is a technique that allows you to connect multiple operations or conditions together in a single line of code. This can make your code more concise, but it can also affect readability.

# Why use it?

# Readability: While chaining can make code shorter, it can also make it harder to understand, especially if the conditions are complex. Therefore, it is important to balance brevity with clarity.

# Usage: Use chaining when you have simple conditions and want to avoid multiple lines of code, but prefer more traditional decision structures when the logic is more complex.

# Without Chaining: The code is longer, but each condition is clear and easy to understand. It is easier to add comments or modify specific parts of the logic.

# Example without chaining
age = 20

if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# With Chaining: The code is more compact, but can be harder to read, especially if the conditions are complex. Readability may be compromised, and code maintenance may become more challenging.

# Example with chaining
age2 = 20

# Using a conditional (ternary) expression for chaining
message = (
    "You are a child."
    if age2 < 13
    else (
        "You are a teenager."
        if age2 < 20
        else "You are an adult." if age2 < 65 else "You are a senior citizen."
    )
)

print(message)
