from functools import lru_cache
from time import perf_counter


@lru_cache(maxsize=3)
def fib(n):
    if n <= 1:
        return n

    return fib(n - 1) + fib(n - 2)


start = perf_counter()
print(f'Fib:{fib(300)}')
end = perf_counter()
print(f'Diff: {end - start}')
