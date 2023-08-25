def parse(s, sep=',', strip=True):
    items = s.split(sep)
    if strip:
        return [i.strip() for i in items]
    else:
        return items


print(parse('    a, b,c    '))
print(parse('a:b: c', sep=':', strip=True))
