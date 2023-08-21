message = "The definitative guide to Python"
print(message.lower())
print(message.upper())
print(message.title())

name = "Bisshwajit "
print(name.rstrip(''))
another = "Nos of Students Students"
print(another.strip())
print(another.strip('Students'))
data = "bisshwajit,samanta"
split_data = data.split(',')
print(split_data)
first_name, last_name = data.split(',')
print(f'First Name {first_name}, Last Name {last_name}')
data_join = ['item1','item2','item3']
print(', '.join(data_join))
print('--'.join('ABCD'))

print('rock' in 'python rocks!')
print('Rock'.casefold() in 'python rocks!'.casefold())

print('Python rocks'.startswith('Python'))
print('Python rocks'.endswith('rocks'))
print('Python rocks'.casefold().endswith('Rocks'.casefold()))

message = "To every action there is an equal and opposite reaction"
print(message.find('every'))
numbers = [1,3,4,5,7]
print(numbers.index(7))
















