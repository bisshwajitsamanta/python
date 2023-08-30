def add(a, b):
    return a + b

def greet(name:str):
    return f'Hello {name}'


def apply(func, *args):
    result = func(*args)
    return result


print(f'Apply Function: {apply(add, 10, 20)}')
print(f'Apply Lambda Function: {apply(lambda a,b,c: a+b+c,10,20,30)}')
print(f'Apply Function Greet: {apply(greet,"Bisshwajit Samanta")}')
