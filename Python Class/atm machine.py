#input
amount = int(input("enter amount: "))

#logic
amount = amount - 100
note_2000 = amount // 2000
amount = amount % 2000
note_500 = amount // 500
amount = amount % 500
note_200 = amount // 200
amount = amount % 200
note_100 = amount // 100 + 1

#output
print("Rs. 2000 notes:", note_2000)
print("Rs. 500 notes:", note_500)
print("Rs. 200 notes:", note_200)
print("Rs. 100 notes:", note_100)