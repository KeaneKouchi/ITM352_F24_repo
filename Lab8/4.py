#Debugging exercise # 4
def get_element(list, index):
    return list[index]


my_list = [1, 2, 3, 4, 5]
print(get_element(my_list, 2))  
# changed the 5 index to a -1 so it uses the last indexed number in the list 
print(get_element(my_list, -1)) 

# alternatively can use 4 to hardcode using the 4th indexed position
#print(get_element(my_list, 4)) 