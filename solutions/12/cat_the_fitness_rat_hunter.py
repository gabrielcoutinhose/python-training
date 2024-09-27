cat_lives_remaining = 0

while cat_lives_remaining <= 3:
    used_life_insurance = str(input("y/n"))
    if used_life_insurance == "y":
        print("")
    else:
        if cat_lives_remaining <= 0:
            print("")
        else:
            print(
                "This cat is lucky! hard to fall! That was close"
            )  # Apply random after
