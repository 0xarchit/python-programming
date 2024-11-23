'''
4. Car Insurance Premium Calculation
Problem: Write a program to calculate car insurance premiums. The premium depends on:
• The car's age:
o Less than 5 years: base premium is $500.
o 5 to 10 years: base premium is $800.
o More than 10 years: base premium is $1200.
• If the car owner is under 25 years old, there’s an additional 20% premium.
• If the car owner has had no accidents in the last year, they get a 10% discount.
Input: car_age, owner_age, no_accidents
'''

car_age= int(input('Enter Car Age in years: '))
owner_age= int(input('Enter Owner Age in years: '))
no_accidents = input('Has the owner had any accidents in the last year? (true/false)')
if no_accidents.lower() == 'true':
    no_accidents = True
else:
    no_accidents = False
if car_age < 5:
    base_premium = 500
elif 5 <= car_age <= 10:
    base_premium = 800
else:
    base_premium = 1200
if owner_age < 25:
    premium = base_premium * 1.2
else:
    premium = base_premium
if no_accidents:
    premium = premium * 0.9
    print(f'The car insurance premium is: $', premium)
else:
    print(f'The car insurance premium is: $', premium)