data = [10, 20, 'abc', 30]
sum_data, count_data = 0, 0
# Try and ask for forgiveness later
try:
    for element in data:
        try:
            sum_data += element
            count_data += 1
        except TypeError:
            # skip abc
            pass
    average = sum_data / count_data
    print(f'Average: {average}')
except ZeroDivisionError as ex:
    average = 0
    print(f'Zero Division Error occurred: {ex}')
    print(f'Average: {average}')

print('Code resumes')
