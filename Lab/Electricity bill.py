'''
5. Electricity Bill Calculation
Problem: Create a program to calculate electricity bills. The billing rules are:
• The first 100 units cost $0.50 per unit.
• The next 100 units (101 to 200) cost $0.75 per unit.
• After 200 units, the cost is $1.20 per unit. If the total bill exceeds $300, a surcharge of
15% is added.
Input: units_consumed
'''

units_consumed=  int(input("Enter the number of units consumed: "))
if units_consumed <= 100:
    bill = units_consumed * 0.5
if 100<units_consumed<=200:
    bill = 50 + (units_consumed - 100) * 0.75
if units_consumed > 200:
    bill = 150 + (units_consumed - 200) * 1.2
if bill > 300:
    bill = bill + (bill * 0.15)
print("Your electricity bill is: ", bill)
