# Day two Assignment
# Tip calculator

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip_percent = float(input("What percentage tip would you like to give? %"))
people = float(input("How many people will be splitting the bill? :"))

per_person_sum = bill * (tip_percent + 100)/ 100 / people
print(f"Each person should pay ${round(per_person_sum, 2)}")