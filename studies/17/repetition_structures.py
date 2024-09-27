"""Repetition structures"""

# FOR
# Ex 1
for say_hello in range(0, 6, 2):
    print("hello", say_hello)

# Ex 2
names = ["Mark", "Apollo", "Cezar", "Louis"]
for name in names:
    print(name)

# Nested loops & iteration
# Ex 1
my_items = [
    "m - 1",
    "m - 2",
    "m - 3",
    "m - 4",
    "m - 5",
    "m - 6",
]
complement_for_my_items = [1, 2, 3, 4, 5, 6]
for item in my_items:
    for complement in complement_for_my_items:
        print(f"{item} {complement}")

# Ex 2
for letter in "test_word":
    print(letter)

# While
# Ex 1
counter = 0
while counter < 3:
    # counter = counter + 1
    counter += 1
    print(f"{counter} continue")
