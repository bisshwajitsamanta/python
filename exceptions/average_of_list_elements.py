# data = [10, 4, 19, 30, 12]
data = []
sum_data, count_data = 0, 0

# Look before you leave pattern.
if len(data) == 0:
    average = 0
else:
    for element in data:
        sum_data += element
        count_data += 1
    average = sum_data / count_data
print(f'Average {average}')
