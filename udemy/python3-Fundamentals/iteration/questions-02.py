data = (
    ['2021-01-01', 10, 20],
    ['2021-01-02', 20, 18],
    ['2021-01-03', -10, 10],
    ['2021-01-04', 100, 142],
    ['2021-01-05', 20, 45]
)
largest_element = []
for index, element in enumerate(data):
    extra_element = element[2]-element[1]
    largest_element.append(extra_element)
    element.append(extra_element)
    print(element)
# largest_element.sort()
# print(f'Largest element is {largest_element[-1]}')
print(f'Largest element is {max(largest_element)}')

