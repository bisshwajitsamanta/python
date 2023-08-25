def product(*values: int) -> int:
    prod = 1
    if len(values) == 0:
        raise ValueError('Must Provide least 1 argument')
    for element in values:
        prod *= element
    return prod


print(product(*[1,2,3,4]))
