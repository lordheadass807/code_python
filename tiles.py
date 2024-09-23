
#imports math, squareoot function and floor 
#floor rounds everything down
from math import sqrt, floor

#input
print("how many tiles does gigi have?")
tiles = int(input())

#processing
#sqrts the # of tiles given and rounds down
answer = sqrt(tiles)
answer = floor(answer)

#output
print(f"the largest square gigi can have is {answer}")