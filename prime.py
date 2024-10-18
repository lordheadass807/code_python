def factorList(num):

     factors = []
     for divider in range(1, num+1):
        if num % divider == 0:
            factors.append(divider)

     return factors


def isPrime(num):

     check = factorList(num)
     if len(check) == 2:
         return True
     else:
         return False


input = 18

print(factorList(input))
print(isPrime(input))

