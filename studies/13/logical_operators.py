# Parentheses
# Through parentheses we say what the order of execution is.
result_parentheses = (2 + 3) * 4
print(f"Parentheses: {result_parentheses}")

# Exponent
result_exponent = 2**3
print(f"Exponent: {result_exponent}")

# Multiplication
result_multiplication = 5 * 4
print(f"Multiplication: {result_multiplication}")

# Division
result_division = 10 / 2
print(f"Division: {result_division}")

# Integer Division
result_integer_division = 10 // 3
print(f"Integer Division: {result_integer_division}")

# Modulus
result_modulus = 10 % 3
print(f"Modulus: {result_modulus}")

# Addition
result_addition = 5 + 3
print(f"Addition: {result_addition}")

# Subtraction
result_subtraction = 10 - 4
print(f"Subtraction: {result_subtraction}")

# Logical Comparators

# In python we can compare different types

# Python is case sensitive; and this becomes clear when we use True or False,
# or when we compare two apparently equal values.

print(True == False)  # False
print("Rafael" == "rafael")  # False
print("a" > "e")
print(10 == "10")  # False; because the value are a different types

equality = 5 == 5
print(f"Equality: {equality}")

inequality = 5 != 3
print(f"Inequality: {inequality}")

greater_than = 5 > 3
print(f"Greater than: {greater_than}")

less_than = 5 < 3
print(f"Less than: {less_than}")

greater_equal = 5 >= 5
print(f"Greater or equal: {greater_equal}")

less_equal = 3 <= 5
print(f"Less or equal: {less_equal}")

# Identity
# depending on the context, IS will return a different result.
# but in the case of comparing == and IS with none; both will be necessary
a = [1, 2, 3]
b = a
identity = a is b
not_identity = a is not [1, 2, 3]
print(f"Identity: {identity}")
print(f"Not identity: {not_identity}")

# Membership
my_list = [1, 2, 3]
membership = 2 in my_list
print(f"Membership: {membership}")
not_membership = 4 not in my_list
print(f"Not membership: {not_membership}")

# NOT boolean
result_not = not True
print(f"NOT boolean: {result_not}")

# AND boolean
result_and = (5 > 3) and (3 > 1)
print(f"AND boolean: {result_and}")

# OR boolean
result_or = (5 > 3) or (3 < 1)
print(f"OR boolean: {result_or}")

# Mixing boolean expressions
a, b, c, d, e = 5, 5, 5, 5, 5
print(((a == b) and (c == d)) or (e == 5))
