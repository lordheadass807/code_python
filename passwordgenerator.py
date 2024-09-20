#introduction to code

import random

print("welcome to our password generator app ")


pwrd_length = int(input("enter the length of the password "))

#possible characters for our value in ASCII
lowercase = list(range(97, 123))
uppercase = list(range(65, 91))
digits = list(range(48, 58))
specialchar = list(range(33, 48)) + list(range(58, 65)) + list(range(91, 97)) + list(range(123, 127))

#possible character
pwrd_symbols = lowercase.copy() 

has_upper = input("include uppercase characters? (yes/no)  ")
if has_upper == "Yes" or has_upper == "yes":
    pwrd_symbols.extend(uppercase)

has_digits = input("include digits? (yes/no)  ")
if has_digits == "Yes" or has_digits== "yes":
    pwrd_symbols.extend(digits)

has_specialchar = input("include special characters? (yes/no)  ")
if has_specialchar == "Yes" or has_specialchar == "yes":
    pwrd_symbols.extend(specialchar)

new_password = ""

#randomizer

while len(new_password) != pwrd_length:
    random_symbol = chr(random.choice(pwrd_symbols))
    new_password = new_password + random_symbol

print(f"{new_password} has been generated")