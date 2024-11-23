'''
6. Shipping Fee Calculation
Problem: Write a program to calculate shipping fees. The rules are:
• If the destination is international, a flat fee of $30 is added.
• If the package weight exceeds 10 kg, an additional charge of $5 per kg over 10 kg is
added.
• Domestic shipments have no additional charges if the weight is under 10 kg.
Input: destination, weight
'''

destination = input("Enter destination (domestic/international): ")
weight = float(input("Enter package weight in kg: "))

if destination.lower() == "international":
    base_fee = 30
else:
    base_fee = 0

if weight > 10:
    additional_fee = (weight - 10) * 5
else:
    additional_fee = 0

total_fee = base_fee + additional_fee

print("Total shipping fee: $", total_fee) 