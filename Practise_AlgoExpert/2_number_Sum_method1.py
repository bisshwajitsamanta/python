"""
    Any 2 integer in an array if equals to the target sum then put them into an array
"""

"""
    Approach:
        1. Take the first element and keep on adding till the length of the array and see if the value is equals to 10
            a. If the value is 10 then put it in a different array and print the result array.
            b. If not then continue adding the 2nd element to the entire list including the first element.
"""

array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10

"""
    We are traversing to 1 last than the number as 6th Index is -1 and we are summing up
    -1 + 6, 7th Index has noithing to sum up so index error will come
"""


def two_number_sum(input_value, target_sum):
    for i in range(len(input_value) - 1):  # Leaving the last index
        first_num = input_value[i]
        for j in range(i+1,len(input_value)):
            second_num = input_value[j]
            if first_num + second_num == target_sum:
                print(first_num,second_num)


two_number_sum(array, 10)
