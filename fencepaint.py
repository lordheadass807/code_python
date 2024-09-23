from math import ceil

side1 = input("enter section 1 ")
side2 = input("enter section 2 ")
side3 = input("enter section 3 ")

cans = len(side1) + len(side2) + len(side3)
boxes = ceil(cans / 12)
leftover = (boxes * 12) - cans
cost = boxes * 14.95

message = f"you need {cans} cans with {leftover} leftover and {cost} dollars"
print(message)