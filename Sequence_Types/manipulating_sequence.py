mylist = [1,2,3,4,5]
mylist[0:3] = ['a','b']
print(mylist)
print(len(mylist))
del mylist[1:3]
print(mylist)

my_list = [1,2,3]
my_list.append(4)
my_list.extend(("hello",5,"world"))
print(my_list)

my_new_list = [3,4,5,7]
my_new_list.insert(2,100)
print(my_new_list)