def dupeRemove(a_list):

    removed_list = []

    for item in a_list:
        if item not in removed_list:
            removed_list.append(item)
    
    return removed_list


List = [1,2,3,4,5,6,6,6,7,6,3,6,4,4,9,9,10]
print(dupeRemove(List))