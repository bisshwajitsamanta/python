def choose_operator(name: str):
    if name == "add":
        return lambda a, b: a + b
    if name == "mult":
        return lambda a, b: a * b
    if name == "power":
        return lambda a, n: a ** n


op = choose_operator('add')
print(f'Choose Operator Result:{op(2, 3)}')
