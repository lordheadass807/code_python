def isAbundant(num):
    
    factors = []

    for divider in range(1, num-1):
     if num % divider == 0:
        factors.append(divider)

    check = sum(factors)

    if check > num:
        return True
    else:
        return False

data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

odd_counter = 0
even_counter = 0

for item in data:
    if isAbundant(item) == True:
        if item % 2 == 0:
            even_counter += 1
        else:
            odd_counter += 1

print(f"the amount of even abundants are {even_counter}")
print(f"the amount of odd abundants are {odd_counter}")