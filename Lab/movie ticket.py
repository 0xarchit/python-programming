'''
1. Movie Ticket Booking System
Problem: You need to implement a ticket pricing system for a cinema. The pricing scheme is
as follows:
• Children (age < 12) get a 50% discount on the ticket price.
• Senior citizens (age ≥ 60) get a 30% discount.
• Adults (12 ≤ age < 60) pay the full ticket price. Also, if the movie is a 3D movie, an
additional charge of $5 is added to the ticket price.
Input: age, ticket_price, is_3d_movie
'''
age= int(input('enter age: '))
ticket_price = float(input('enter ticket price: '))
is_3d_movie  = input('is it 3d movie? (true/false): ')
if age < 12:
    discount = 0.5
elif age >= 60:
    discount = 0.3
else:
    discount = 0
price = ticket_price * (1 - discount)
if is_3d_movie.lower() == 'true':
    price += 5
print(price)
