# The welcoming greeting
greeting = "Welcome to the tip calculator!"
print(greeting)
# collecting the input values for calculation
bill = input("What was the total bill? $ ")
tip = input("How much tip would like like to get? 10, 12, 15? ")
people = input("How many people to split the bill? ")
# converting the input string data integers
bill_as_int = int(bill)
tip_as_int = int(tip)
people_as_int = int(people)
# calculations
total_tip = 1 + (tip_as_int / 100)
bill_per_person = round((bill_as_int * total_tip) / people_as_int, 2)
# converting the result display exactle 2 decimal points even when there is no value at the second dp
final_amount = "{:.2f}".format(bill_per_person)

pay_statement = f"Each person should pay: $ {final_amount}"

print(pay_statement)