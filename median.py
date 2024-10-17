def median(a_list):
    
     sorted_list = sorted(a_list)
     m = len(a_list) // 2
    #.sort() is worse, it directly mutates the original varible

     if len(a_list) % 2 == 0:
        left = a_list[m-1]
        right = a_list[m]
        average = (left+right) / 2
        return average

     else:
        return a_list[m]


data = [3,1,4,7,6,9]
print(median(data))
