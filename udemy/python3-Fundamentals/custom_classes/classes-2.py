class Person:
    def __init__(self):
        print("Custom Init")

p1 = Person()
print(p1)

class NewPerson:
    def __init__(self,first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

p2 = NewPerson('Bisshwajit','Samanta')
print(p2.first_name)
print(p2.__dict__)