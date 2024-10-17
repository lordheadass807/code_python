
factors = []
num = int(input("enter a number: "))

for divider in range(1, num-1):
    if num % divider == 0:
        factors.append(divider)

check = sum(factors)

if check > num:
    print(f"your number {num} is an abundant number")

elif check < num:
    print(f"your number {num} is an deficiant number")

else:
    print(f"your number {num} is a perfect number")



