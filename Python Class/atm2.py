amount=int(input("enter amount: ")) - 500

note_2000 = amount // 2000
amount = amount % 2000
note_500 = amount // 500+1
amount = amount % 500

print("2000 notes:", note_2000)
print("500 notes:", note_500)