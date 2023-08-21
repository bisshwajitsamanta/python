m = [[0,0,0] for _ in range(3)]
print(m)

# Identity Matrix
m1 = [
    [1 if row == col else 0 for col in range(3)]
    for row in range(3)
]
print(m1)
m2 = [
    [1 for col in range(3) if row == col ]
    for row in range(3)
]
print(m2)