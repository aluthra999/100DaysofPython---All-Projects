bill = float(input("What was your total bill: "))
tip = int(input("How much tip you want to give? 5%, 10%, 15%, 20%: "))
people = int(input("Total people to split the bill: "))

tip_percent = tip / 100
tip_amount = tip_percent * bill
total_bill = bill + tip_amount
per_person = total_bill / people

print(f"Total bill was: {bill}")
print(f"Tip added: {tip_amount}")
print(f"Total bill after tip: {total_bill}")
print(f"Bill is {per_person} per person")
