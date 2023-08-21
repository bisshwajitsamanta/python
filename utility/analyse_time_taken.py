from time import perf_counter_ns

start = perf_counter_ns()
l = range(100_000_000)
end = perf_counter_ns()
print(f'Time Elapsed {end - start}')