from time import perf_counter


def factorial(n):
    prod = 1
    for i in range(1, n + 1):  # runs 3 times for value of 4
        prod = prod * i
    return prod


def diagonal_matrix(rows, cols, *, diagonal=1):
    return [[diagonal if row == col else 0 for col in range(cols)] for row in range(rows)]


def time_it(func):
    def inner(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        print(f'Elapsed Time:: {end - start}')
        return result

    return inner


timed_fact = time_it(factorial)
result = timed_fact(4)
print(f' Result is ::{factorial(4)}, and Time Taken : {result}')
timed_diagnoal = time_it(diagonal_matrix)
result_diagonal = timed_diagnoal(1,1)
print(f' Result is ::{diagonal_matrix(1,1)}, and Time Taken : {result_diagonal}')
