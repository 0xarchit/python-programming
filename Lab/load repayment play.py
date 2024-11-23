'''
9. Loan Repayment Plan
Problem: Design a program to determine a person's loan repayment plan. The conditions are:
• If the loan amount is less than $50,000, they must repay it within 5 years.
• If the loan amount is between $50,000 and $100,000, they must repay it within 10
years.
• If the loan amount is greater than $100,000, they must repay it within 15 years.
• Additionally, if the person’s annual income is less than $30,000, they are allowed an
extra 2 years to repay.
Input: loan_amount, annual_income
'''
loan_amount= int(input("Enter Loan Amount: "))
annual_income= int(input("Enter Annual Income: "))
if loan_amount < 50000:
    if annual_income < 30000:
        print("Repayment Period: 7 years")
    else:
        print("Repayment Period: 5 years")
if  loan_amount >= 50000 and loan_amount <= 100000:
    if annual_income < 30000:
        print("Repayment Period: 12 years")
    else:
        print("Repayment Period: 10 years")
if loan_amount > 100000:
    if annual_income < 30000:
        print("Repayment Period: 17 years")
    else:
        print("Repayment Period: 15 years")