def average(*value):
    if len(value) == 0:
        return 0
    return sum(value)/len(value)

print(f'Average: {average(0,1,2,3,4)}')

def list_print(*value):
    return value

print(f'List: {list_print([1,2,3,4])}')