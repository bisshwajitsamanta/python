class Person:
    """
    This string can be used to document this class.
    """


p1 = Person()
p1.name = 'Bisshwajit' # Get/ set attributes on custom objects.
print(p1.__doc__)
print(p1.__class__)
print(p1.__dict__)
print(p1.name)
del p1.name
print(p1.name)
