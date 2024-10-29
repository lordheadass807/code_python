def factor_count(number):

     factors = []

     for divider in range(1, number):
         if number % divider == 0:
             factors.append(divider)


     return factors

def k_value(number, k):

     factors = factor_count(number)
      
     if k <= len(factors):
        return factors[k - 1]

     else:
        return "out of range"




n = int(input("enter a number "))
k = int(input("enter a number "))

print("factors are:", factor_count(n))
print("the kth position is",  k_value(n, k))





        
