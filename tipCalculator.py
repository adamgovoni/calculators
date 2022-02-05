# This is a basic tip calculator
# Inputs are for total bill then desired tip%
# The output states the desired tip on the given bill then how much the server will receive
# and finally the total bill with tip included.

def tip_calc(bill_amount, tip_perc):
    tip_total = bill_amount * (0.01 * tip_perc)
    tip_total = '$' + str(format(tip_total, '.2f'))
    total = bill_amount * (1+0.01 * tip_perc)
    total = '$' + str(format(total, '.2f'))
    bill_amount = '$' + str(format(bill_amount, '.2f'))
    return tip_perc, bill_amount, tip_total, total


bill = float(input("Enter bill amount: $"))
tip = int(input("Enter tip%: "))

tip_perc, bill_amount, tip_total, total = tip_calc(bill, tip)

print(f"Choosing a {tip_perc}% tip on a {bill_amount} bill,")
print(f"your server receives a {tip_total} tip.")
print(f"Total to pay:  {total}")

