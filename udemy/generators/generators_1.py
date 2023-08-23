list_squares = [i **2 for i in range(1,5)]
print(list_squares)

generator_squares = (i **2 for i in range(1,5))
for i in generator_squares:
    print(i)