"""random number"""

import random

print(random.random())

print(random.uniform(6, 11))

print(random.randint(2, 8))

names = ["Gabriel", "Daniel", "Apollo", "Bruce Wayne", "Thomas", "Mathew"]
print(random.choices(names, k=3))

my_numbers = [1, 2, 3, 4, 5, 6]
print(my_numbers)
print(random.shuffle(my_numbers))
