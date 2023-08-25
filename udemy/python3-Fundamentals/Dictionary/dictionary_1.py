from copy import deepcopy
data = {
    'open': 100,
    'high': 110,
    'low':95,
    'close':110
}

found = 'open' in data
not_found = 'dummy' in data
print(found)
print(not_found)
print(f'Length of data {len(data)}')

d = {
    'a': [1,2,3,4],
    'b': {
        'x': 0,
        'y': 1
    }
}
d['a'].append(4)
shallow_copy = d.copy()
deep_copy = deepcopy(d)
deep_copy['a'].append(5)
print(f'Dictionary Elements: {d} \nShallow Copy Elements: {shallow_copy}')
print(f'Dictionary Elements: {d} \nDeep Copy Elements: {deep_copy}')