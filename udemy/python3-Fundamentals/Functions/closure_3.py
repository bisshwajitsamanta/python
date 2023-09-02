def power(n):
    def inner(x):
        return x ** n
    return inner

squares = power(4)
cubes = power(3)
print(f'Squares:{squares(2)}')
