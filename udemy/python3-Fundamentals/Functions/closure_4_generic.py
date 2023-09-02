def execute(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        return result

    return inner


def add(a, b, c):
    print('add ...')
    return a + b + c


def greet(name, *, Formal=True):
    print('Greet ...')
    if Formal:
        return f'Pleased to meet you {name}'
    else:
        return f'Hi {name}'


execute_add = execute(add)
print(f'Addition: {execute_add(2,3,4)}')

execute_greet = execute(greet)
print(f'Greetings: {execute_greet("Bisshwajit",Formal=True)}')
