data = ['a','abcd','asdfar','xzy']
lenghts = [len(el) for el in data]
print(lenghts)

new_length = map(len,data)
print(f'New Length list:{list(new_length)}')