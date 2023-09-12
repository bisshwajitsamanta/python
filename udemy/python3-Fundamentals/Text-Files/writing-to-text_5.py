file_name = "test.csv"

data = ['line1','line2','line3']

with open(file_name,'w') as f:
    f.write('abc')
    f.write('1234')

with open(file_name) as f:
    print(f.readlines())

with open(file_name, 'w') as f:
    f.writelines(data)

with open(file_name) as f:
    print(f.readlines())

with open(file_name, 'w') as f:
    f.write('\n'.join(data))

with open(file_name) as f:
    print(f.readlines())