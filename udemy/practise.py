
# Even Number practise
number_list = [1,2,3,4,5,6,7,8,9,20,40]
even_numbers = [num for num in number_list if num %2 == 0]
even_squares = [num for num in number_list if num %2 ==0 if num <10 ]
print(even_numbers,even_squares)