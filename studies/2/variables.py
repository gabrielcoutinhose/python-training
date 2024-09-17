"""
An overview of variables and data types
"""

# The definition

# When I create and assign a value to a variable, this process is called
# memory allocation.

# We have two options: the variable, which is mutable, and the constant,
# which is immutable during the execution of the program (if it is in
# memory and not in a database).

# Using the variable 'constant' in uppercase is a convention for non-mutable variables;
# although Python does not use the concept of constants.

# Variable
current_vehicle_speed = 20  # pylint: disable=C0103
print(current_vehicle_speed)

# Constant
START_VEHICLE_SPEED = 10
print(START_VEHICLE_SPEED)

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
text = "recommended"
text_two = "two"  # ''
text_three = """three
test"""
text_four = "text for"
text_five = "text five"
print(text, text_two, text_three, text_four, text_five)
# Escape characters
print("text \n six")  # Wrap outline
print("text ' seven'")  # ignore a characters
print("text \\ eight")  # show a \
# Know a string length
test_name = "Daniel"
print(len(test_name))  # print the number of characters on this string

# Lists (list): Ordered and mutable collections of items, which can be of
# different types, such as [1, 2, 3] or ["a", "b", "c"].
list_example = [1, 2, 3, "four", True]
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
    """class that represents a person object"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        """method that makes the person introduce themselves"""
        return f"Hello, my name is {self.name} and i have {self.age} old."


# Creating an instance of the Person class
person = Person("Maria", 25)

# Accessing attributes
print(person.name)  # Output: Maria
print(person.age)  # Output: 25

# Calling a method
print(person.greet())  # Output: Hello, my name is Maria and I am 25 years old.


# Arrays: While lists are commonly used, the NumPy library offers arrays
# that are more efficient for mathematical and scientific operations.

# pip install numpy

# import numpy as np

# creating a NumPy array
# array_a = np.array([1, 2, 3, 4, 5])
# array_b = np.array([6, 7, 8, 9, 10])

# Showing the arrays
# print("Array A:", array_a)
# print("Array B:", array_b)

# Performing mathematical operations
# sum = array_a + array_b
# product = array_a * array_b
# mean = np.mean(array_a)

# Showing the results
# print("Sum:", sum)
# print("Product:", product)
# print("Average of Array A:", average)


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
