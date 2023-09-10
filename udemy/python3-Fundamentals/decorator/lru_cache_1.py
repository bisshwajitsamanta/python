def cache(func):
    cache_dict = {}

    def inner(*args):

        if args in cache_dict:
            print('Cache Hit')
            return cache_dict[args]
        else:
            print('Cache Miss')
            result = func(*args)
            cache_dict[args] = result
            return result

    return inner


@cache
def add(a, b):
    return a + b


print(f'Addition:{add(1, 2)}')
print(f'Addition:{add(1, 2)}')
