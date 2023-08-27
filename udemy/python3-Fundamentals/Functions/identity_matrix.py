# without lambda

def identity(rows, cols):
    return [[1 if row == col else 0 for col in range(cols)] for row in range(rows)]


print(identity(5, 5))

# With Lambda

f = lambda rows,cols: [[1 if row == col else 0 for col in range(cols)] for row in range(rows)]
print(f(5,5))
