"""
    Approach 2 :  Store the Numbers in a Map if the value is seen then return
            x + y = 10 ( 10 = target Sum)
            x = the current number iteration in the array
            y = we need to find the number
            so, y = 10 -x
            If we have seen y in the map then return x and y
            Time Complexity = O(N)
            Space Complexity = O(N)

"""

array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10


def two_number_sum(input_value, target_sum):
    nums = {}
    for i in input_value:
        potential_match = target_sum - i
        if potential_match in nums:
            print(potential_match,i)
            return [potential_match,i]
        else:
            nums[i] = True

    return []


two_number_sum(array,targetSum)