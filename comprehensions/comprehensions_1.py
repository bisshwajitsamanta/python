numbers = [1,2,3,4,5,6]
sq = []
for num in numbers:
    sq.append(num **2)
print(sq)

sq1 = [ num **3 for num in numbers]
print(sq1)