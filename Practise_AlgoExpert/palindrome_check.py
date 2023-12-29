"""
    Palindrome Check in Python
    string = "abcdcba"
"""


def is_palindrome(input_value):
    if input_value != "":
        reverse_value = input_value[::-1]
        print(reverse_value)
        if input_value == reverse_value:
            print("This is a Palindrome")
    else:
        print("Input is empty")


is_palindrome("abcdcba")
