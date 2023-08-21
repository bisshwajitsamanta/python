name = input("Enter name: ")

if len(name)<5:
    raise ValueError('Name must be 5 characters long ...')
else:
    print(f'Hello {name}!')

print(issubclass(KeyError,LookupError))
print(issubclass(IndexError,LookupError))
print(issubclass(LookupError,Exception))

ex = KeyError("Some message")
print(type(ex))

print(isinstance(ex,LookupError))
print(isinstance(ex,Exception))
print(isinstance(ex,KeyError))
print(isinstance(ex,IndexError))