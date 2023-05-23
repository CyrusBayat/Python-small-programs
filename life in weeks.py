

current_age = input("What is your current age?\n")

age_goal = input("What is you traget age to live? \n")

age_left = int(age_goal) - int(current_age)

days = age_left * 365

weeks = age_left * 52

months = age_left * 12

print(f"you have {days} days, {weeks} weeks, and {months} months left.\n")