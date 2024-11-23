'''
8. Tax Filing Status Determination
Problem: Write a program that determines a person's tax filing status. The rules are:
• If the person is married, their filing status is "Married".
• If the person is single, but has dependents, their status is "Head of Household".
• If the person is single and has no dependents, their status is "Single".
Input: married, has_dependents
'''
married=input("enter married status(True/Flase): ")
has_dependents=input("enter dependents status(True/Flase): ")
if married=="True":
    print("Married")
elif married=="True" and has_dependents=="True":
    print("Head Of Household")
else:
    print("Single")