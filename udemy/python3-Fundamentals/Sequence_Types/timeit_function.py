from timeit import timeit
l = []
print(timeit('l.append(1)',globals=globals(),number=100_000))

lis = []
print(timeit('l.insert(0,1)',globals=globals(),number=100_000))