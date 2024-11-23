'''
2. Credit Card Fraud Detection
Problem: Develop a fraud detection system for a bank. The system should flag a transaction
as "suspicious" if:
• The transaction amount exceeds 70% of the account's total balance.
• The transaction happens after 10 PM (22:00) or before 6 AM (06:00).
Input: account_balance, transaction_amount, transaction_time (24-hour format)
'''

account_balance = float(input('enter account balance: '))
transaction_amount =  float(input('enter transaction amount: '))
transaction_time = int(input('enter time in 24 hour formate:'))

if  transaction_amount > (account_balance * 0.7):
    print('suspicious transaction')
elif transaction_time < 6 or transaction_time > 22:
    print('suspicious transaction')
else:
    print('safe transaction')