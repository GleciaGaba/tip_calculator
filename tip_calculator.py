# If the bill was $150.00, split between people, with 12% tip.
# Each person should pay (150.00/5) * 1.12 = 33.6
# Format the result to 2 decimal places  = 33.60
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.
# Write your code below this line.


print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill?\n"))
tip = int(input("How much tip would you like to give?10%, 12%, or 15%? \n"))
people = int(input("How many people to split the bill?\n"))

if tip == 10:
    result = total_bill / people * 0.10
elif tip == 12:
    result = total_bill / people * 0.12
elif tip == 15:
    result = total_bill / people * 0.15
else:
    result = 'Error'

total_result = total_bill / people + result

print(f"The tip amount divided for each person is :{round(result, 2)}")
print(f"Each person should pay: {round(total_result, 2)}")
