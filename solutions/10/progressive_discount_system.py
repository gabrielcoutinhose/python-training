"""progressive_discount_system"""

print("Hello! welcome to; best shop!")

print("This is our system, for apply a progressive discounts in your invoice")

print("Our offers is basically These:")
print("To buy from 100$ you can save 1%")
print("To buy from 200$ you can save 2%")
print("To buy from 300$ you can save 3%")
print("To buy from Above 400$ you can save 4%")

are_a_veteran = str(
    input("You are a veteran? plus 4% - (y/n) - and input your Army-ID")
)

blood_donor = str(input("And blood donor? plus 2% - (y/n) and input your Donor-ID"))

member_of_the_offers_club = str(
    input("Are you part of the offers club? plus 1% - (y/n) - and input your Member-ID")
)

total = float(input("What is the gross value of your invoice?"))

if total >= 100 and total <= 200:
    print("")

elif total >= 200 and total <= 300:
    print("")

elif total >= 200 and total <= 300:
    print("")

elif total >= 200 and total <= 300:
    print("")

else:
    print("")

print(f"Ok, your final invoice value, after applying the discounts and: {total} %")
print("Thank you for your preference!")
