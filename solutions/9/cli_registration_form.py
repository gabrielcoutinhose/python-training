# CLI Registration Form

import datetime
import random

print("Hello! Welcome to the registration step.")
print("Now to get started, we need some information from you.")
print("Let's go!")

# Ask for the full name
full_name = input("What's your full name? ")
print("Full name was saved.")

# Ask for the date of birth
date_of_birth = datetime.datetime.strptime(
    input("What is your date of birth? (MM/DD/YYYY): "), "%m/%d/%Y"
)
formatted_date_of_birth = date_of_birth.strftime("%m/%d/%Y")
print("Date of birth was saved and formatted.")

# Calculate age
age = (datetime.datetime.now() - date_of_birth).days // 365  # Calculate age in years
print(f"You are {age} years old.")

# Ask for the ID number
number_id = input("Your number ID? ")
print("Your ID was saved.")

# Select a random team
possible_teams = ["A", "B", "C", "D", "E"]
team_name = random.choice(possible_teams)  # Use choice to select a single team
print(f"Your team '{team_name}' has been selected.")

# Save the registration date
registration_date = datetime.datetime.now()
formatted_registration_date = registration_date.strftime("%m/%d/%Y")
print("Registration date saved.")

# Simulated database
db_simulation = {
    "full_name": full_name,
    "date_of_birth": formatted_date_of_birth,
    "age": age,
    "number_id": number_id,
    "team_name": team_name,
    "registration_date": formatted_registration_date,
}
print("Data registered successfully.")

# Presentation of the data
print(
    f"Hello {full_name}, you were born on {formatted_date_of_birth}, "
    f"you are {age} years old, your number ID is {number_id}, "
    f"your team is '{team_name}', and your registration date is {formatted_registration_date}. "
    "Thanks, and welcome to the team!"
)
