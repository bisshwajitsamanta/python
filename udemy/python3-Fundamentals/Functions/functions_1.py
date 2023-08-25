def say_hello():
    return 'Hello !'


f = say_hello()
b = say_hello
print(f)
print(b())
print(b is say_hello)
print(globals())
