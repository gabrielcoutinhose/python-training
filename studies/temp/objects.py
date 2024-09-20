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
