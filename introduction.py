firstname = input("what is your first name? ")
lastname = input("what is your last name? ")
age = int(input("what is your birthyear? "))

legal_age = 2024 - age
message = f"hello {firstname} {lastname} you are {legal_age} years old"

if legal_age >= 19:
    print(message)
    print("you are old enough to drink")

else:
    print(message)
    print("you are not old enough to drink")