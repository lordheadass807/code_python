
def average(a_list):
    
    return sum(a_list) / len(a_list)



from random import seed
from random import randrange

seed(2)
data = [randrange(1,100) for _ in range (randrange(10,30))]
print(f'original data set: {data}')
print(f'mean of our date set: {average(data)}')