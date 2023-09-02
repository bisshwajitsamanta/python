def outer(a, b):
    def inner(c):
        return c ** 2

    return inner


func = outer(23, 34)
print(f'Inner Function Square:{func(10)}')
