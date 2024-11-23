'''
10. Ticket Upgrade Decision
Problem: Create a program that determines if a person can upgrade to a higher class on a
flight. The conditions are:
• A person can upgrade if they have enough points (at least 1000).
• If the flight is overbooked, they need 20% fewer points (800).
• If they are a frequent flyer, they need 10% fewer points (900), and 30% fewer if the
flight is also overbooked (700).
Input: points, is_overbooked, is_frequent_flyer
'''
points= int(input('enter number of points: '))
is_overbooked = input('is flight overbooked? (true/false): ').lower
is_frequent_flyer = input('is person a frequent flyer? (true/false): ')
if is_overbooked == 'true' and is_frequent_flyer == 'true':
    if points >= 700:
        print('Upgrade possible')
    else:
        print('Upgrade not possible')
elif is_overbooked == 'true':
    if points >= 800:
        print('Upgrade possible')
    else:
        print('Upgrade not possible')
elif is_frequent_flyer == 'true':
    if points >= 900:
        print('Upgrade possible')
    else:
        print('Upgrade not possible')
else:
    if points >= 1000:
        print('Upgrade possible')
    else:
        print('Upgrade not possible')
