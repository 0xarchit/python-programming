'''
3. Online Shopping Discount System
Problem: Design a discount system for an online shopping platform. The discount rules are:
• If the purchase is above $200, the customer gets a 15% discount.
• For purchases between $100 and $200, they get a 10% discount.
• If the customer is a premium member, they get an additional 5% discount on top of
the initial discount.
Input: purchase_amount, is_premium_member
'''
purchase_amount=float(input('enter purchase amount: '))
is_premium_member=input('is premium member? (true/false): ')
if purchase_amount >200:
    discount=0.15
elif 100<=purchase_amount<=200:
    discount=0.10
else:
    discount=0.00
if  is_premium_member.lower()=='true':
    discount+=0.05
final_amount = purchase_amount - (discount*purchase_amount)
print("Total Price after discoumt: ", final_amount)

