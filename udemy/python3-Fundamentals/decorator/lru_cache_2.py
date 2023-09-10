from functools import lru_cache


@lru_cache(maxsize=2)
def add(a, b):
    print(f'Function called:{add.__name__}')
    return a + b


print(f'Cache: {add(1, 2)}')
print(f'Cache: {add(1, 2)}')
