numbers = [1.0, 2.0, 3.0, 4.0]


def corrected_value(value):
    return value * 32


# List method
listed_value = [corrected_value(i) for i in numbers]
print(listed_value)

# map method
listed_map = map(corrected_value, numbers)
print(list(listed_map))
