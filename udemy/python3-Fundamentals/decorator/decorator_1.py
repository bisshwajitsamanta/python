def wrapper(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)  # unpacking the *args and **kwargs
        print(f'Function Name: {func.__name__}')
        return result

    return inner

@wrapper
def add(a, b, c):
    return a + b + c


# add = wrapper(add)
@wrapper
def greet(name):
    return f'Hello {name}!!'


# greet = wrapper(greet)
@wrapper
def join(data, *, item_sep=",", line_sep="--"):
    return line_sep.join([
        item_sep.join(str(item) for item in row)
        for row in data
    ])


# join = wrapper(join)
# add_wrapper = wrapper(add)
# join_wrapper = wrapper(join)

# print(f'Add of the numbers: {add_wrapper(1, 2, 3)}')
# print(f'Greetings : {wrapper(greet)("Bisshwajit")}')
# print(f'JOin : {join_wrapper([[1, 2, 3], [4, 5, 6], [7, 8, 9]])}')
print(f'Add of the numbers: {add(1, 2, 3)}')
print(f'Greetings : {greet("Bisshwajit")}')
print(f'JOin : {join([[1, 2, 3], [4, 5, 6], [7, 8, 9]])}')
