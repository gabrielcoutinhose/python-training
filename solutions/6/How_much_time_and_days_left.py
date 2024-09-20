"""How much time and days left?"""

from datetime import datetime

date_now = datetime.now()

inputed_date = datetime.strptime(input("desired date, HH/DD/MM/YYYY: "), "%m/%d/%Y")

time_remaining = inputed_date - date_now
print({time_remaining})
