values = [1,2,3,4]
try:
    minimum = abs(values[0])
    for value in values[1:]:
        if abs(value) < minimum:
            minimum = abs(value)
except IndexError:
    minimum = 0
print(f'Minimum is {minimum}')