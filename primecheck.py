def factors(num):
    result = []

    for divider in range(1, num+1):
     if num % divider == 0:
        result.append(divider)

    return result

def is_Prime(num):

    if len(factors(num)) == 2:
        return True
    else:
        return False

print(factors(20))
print(is_Prime(20))

