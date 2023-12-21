"""
    Any 2 integer in an array if equals to the target sum then put them into an array
"""

"""Approach: 1. Traverse through the list take the first num and add all numbers matching 10, similarly 2nd num and 
all numbers to match 10 a. Take the first number in the array in one for loop as i to length of the array -1 b. Start 
the Loop from i+1 to length of the array and store as 2nd num c. Add both the numbers to see if it matches target sum.
        
        Time Complexity = O(n2) [N square because we are going with 2 for loops ]
        Space Complexity = O(n2) [N square because we are going with 2 for loops ]         
                
            
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
