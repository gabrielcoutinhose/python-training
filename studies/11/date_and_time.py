"""Date and time"""

# Through the datetime() methods, you can choose different information to display

from datetime import datetime

# print(datetime.now())

# # Code input
# my_data = datetime(2000, 2, 2)
# print(my_data)

# BR pattern
# Console input
inputed_date = datetime.strptime(input("desired date, 00/00/0000: "), "%d/%m/%Y")
print(type(inputed_date))

# Days remaining between today and desired date
desired_date = inputed_date
date_now = datetime.now()
time_remaining = desired_date - date_now
print(time_remaining)
