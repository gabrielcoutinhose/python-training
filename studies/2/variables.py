"""
An overview of variables and data types
"""

# The definition

# When I create and assign a value to a variable, this process is called
# memory allocation.

# We have two options: the variable, which is mutable, and the constant,
# which is immutable during the execution of the program (if it is in
# memory and not in a database).

# Variable
print(current_vehicle_speed=20)

# Constant
const = print(start_vehicle_speed=0)

# Unpacking process
vehicle_one_power, vehicle_two_power = 1.0, 2.5
print(vehicle_one_power, vehicle_two_power)

# How can I check the data type?
print(type(vehicle_one_power))

# What data types can we use in Python?

# 1 - Numbers
# Integers (int): Whole numbers, such as 1, 2, 3.
print(integer=10)  # Output: 10

# Floating point (float): Numbers with decimal places, such as 1.5, 2.0.
print(floating_point=3.14)  # Output: 3.14

# Complex numbers (complex): Numbers in the form a + bj, where a and b are floats.
print(complex_number=2 + 3j)  # Output: (2+3j)

# Strings (str): Sequences of characters, such as "Hello, world!".
print(text="Hello, world!", text_two="hello world")  # Output: Hello, world!

# Lists (list): Ordered and mutable collections of items, which can be of
# different types, such as [1, 2, 3] or ["a", "b", "c"].
list_example = [1, 2, 3, "four"]
print(list_example)  # Output: [1, 2, 3, 'four']

# Tuples (tuple): Ordered and immutable collections of items, such as (1, 2, 3).
tuple_example = (1, 2, 3)
print(tuple_example)  # Output: (1, 2, 3)

# Sets (set): Unordered collections of unique items, such as {1, 2, 3}.
# print(set_example={1, 2, 3, 3})  # Output: {1, 2, 3} (duplicate items are removed)

# Dictionaries (dict): Collections of key-value pairs, such as {"name": "John", "age": 30}.
dictionary = {"name": "John", "age": 30}
print(dictionary)  # Output: {'name': 'John', 'age': 30}

# Booleans (bool): Represent truth values, True or False.
print(true_value=True)  # Output: True
print(false_value=False)  # Output: False


# Objects: In Python, you can create your own classes and objects,
# allowing for the manipulation of complex data.
class Person:
    """
    ...
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person("Maria", 25)
print(person.name)  # Output: Maria


# Arrays: While lists are commonly used, the NumPy library offers arrays
# that are more efficient for mathematical and scientific operations.
class Person2:
    """
    ...
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person2("Maria", 25)
print(person.name)  # Output: Maria

# DataFrames: The Pandas library allows you to work with data tables,
# which are very useful for data analysis.
# import pandas as pd

# data = {"name": ["Ana", "Bruno", "Carlos"], "age": [23, 34, 45]}
# dataframe = pd.DataFrame(data)
# print(dataframe)
# Output:
#     name  age
# 0   Ana   23
# 1 Bruno   34
# 2 Carlos  45
