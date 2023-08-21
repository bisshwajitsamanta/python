
my_list = [1,2,3,4]
my_copy = my_list[:3]
my_new_list = [9,8,7,6]
another_list = my_new_list.copy()
print(my_copy)
another_list.append(12)
print(another_list)
print(my_new_list)