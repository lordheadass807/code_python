def factor_count(number, k):

     factors = []

     limit  = int(number**0.5) + 1

     for divider in range(1, limit):
         if number % divider == 0:
             factors.append(divider)
             quotient = n // divider
             if divider != quotient:
                factors.append(quotient)
    
     factors.sort()

     if k <= len(factors):
        return factors[k - 1]
       

     else:
        return "out of range"



n = int(input("enter a number "))
k = int(input("enter a number "))

print("the kth position is",  factor_count(n, k))





        
