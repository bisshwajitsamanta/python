"""
    |     |
    abcdcba => Left pointer a is matching with right pointer a if not match then not palindrome

"""


def is_palindrome(string):
    leftidx = 0
    rightidx = len(string) - 1
    while leftidx < rightidx:
        if string[leftidx] != string[rightidx]:
            return False
        leftidx += 1
        rightidx -= 1
    return True


print(is_palindrome("abcdcba"))
