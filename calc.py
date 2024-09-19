print("welcome to my first calculator app")


num1 = int(input("Enter your first number:  "))
num2 = int(input("Enter your second number:  "))

choice = input("what operation would you like? Addition, Multiplication, Subtraction or Divison? ")

if choice == "Addition":
    print(num1 + num2)
elif choice == "Subtraction":
    print(num1 - num2)
elif choice == "Multiplication":
    print(num1 * num2)
elif choice == "Division":
    print(num1 / num2)

else:
    print("Invalid Operation")


