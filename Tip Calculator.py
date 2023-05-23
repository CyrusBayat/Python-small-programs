# Tip calculator.

print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))

tip = int(input("What persentage tip would you like to give? 10, 12, or 15? % "))

people_N = input("How many people to split the bill? ")

bill_share = (bill / int(people_N))

tip_share = (bill_share * ( tip/100 +1)) - bill_share

totll_sahre = round(tip_share + bill_share, ndigits=4)

print(f"Bill share for each person is ${bill_share} and tip share for each person is $", format(tip_share, ".2f"))
print(f"Each person should pay: $", format(totll_sahre, ".2f"))