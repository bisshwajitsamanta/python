data = list(range(1, 11))

"""is_even is a predicate function, a predicate functions are those who returns true or false value  boolean. Filter 
is a generator meaning one time gives you the values next time it is empty. It is a lazy iterator. It is similar to 
generator"""


def is_even(n):
    return n % 2 == 0


evens = filter(is_even, data)
print(f'evens: {list(evens)}')
print(f'evens: {list(evens)}')

# Another way using lambda function

print(f'Even Numbers List: {list(filter(lambda x: x%2 ==0, data))}')
