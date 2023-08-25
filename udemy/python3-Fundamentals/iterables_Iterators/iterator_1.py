data = [1,2,3,4,5]
iterator = iter(data)

try:
    while True:
        element = next(iterator)
        print(element)
except StopIteration:
    print('All done')
    pass
