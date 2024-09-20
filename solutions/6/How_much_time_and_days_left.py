"""How much time and days left"""

from datetime import datetime

date_now = datetime.now()

inputed_date = datetime.strptime(input("Desired date (MM/DD/YYYY): "), "%m/%d/%Y")

time_remaining = inputed_date - date_now

days_remaining = time_remaining.days
hours_remaining = time_remaining.seconds // 3600

print(f"Days remaining: {days_remaining}, Hours remaining: {hours_remaining}")
