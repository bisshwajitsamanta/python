data = [10,20,30,-10,40,-5]

for t in enumerate(data):
    print(t)


# Unpacking the tuple
for index, element in enumerate(data):
    if element <0:
        data[index]=0
print(data)