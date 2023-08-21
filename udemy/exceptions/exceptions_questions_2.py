try:
    raise ValueError ('Custom Message')
except ValueError as ex:
    print(f'Value error: {ex}')