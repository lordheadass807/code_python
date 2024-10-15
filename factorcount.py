

def factor_count(number):

    '''checks the factor counts of a number

    Args:
    number is an integer

    Returns: number of factors in a number

    '''

    counter = 0
    for divider in range(1, number+1):
        if number % divider ==0:
            counter += 1 

    return counter

#user enters a number, for each number before and including that number it runs factor_count and prints the number of factors in each one

upper_limit = int(input("enter a number"))

for num in range(1, upper_limit+1):
    factor_size = factor_count(num)

    print(f"{num} has {factor_size} factors ")