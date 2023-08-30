from collections import Counter
data = "Ssamanta"
#
value = dict(Counter(data.casefold()))
print(f'Value: {value}')

d = {}
for el in data.casefold():
    d[el] = d.get(el,0)+1
print(f'Elements: {d}')

