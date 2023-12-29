def is_palindrome(string):
    reversed_char = []
    for i in reversed(range(len(string))):
        reversed_char.append(string[i])

    print("".join(reversed_char))
    return "".join(reversed_char) == string


print(is_palindrome("abcdcba"))
