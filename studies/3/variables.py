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
