# Replace None as the average of the elements
data = [1,2,3,None,4,5,None]

count, total = 0,0

for v in data:
    if v is not None:
        count += 1
        total += v
    average = total/count
# print(f'count={count}, average={average}')

# for index, element in enumerate(data):
#     if data[index] == None:
#         element = average
#     print(f'index={index} element={element}')

for index, val in enumerate(data):
    if val is None:
        data[index]= average
print(data)