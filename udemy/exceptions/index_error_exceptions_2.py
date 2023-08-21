l = (1,2,3,4,5)
try:
    while True:
        print(l.pop())
except AttributeError as ex:
    print(f'Cannot Popped out {type(ex)}')
print('Code resumes')
print(l)