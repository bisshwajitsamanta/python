list = [1,2,3,4,5]

# try:
#     while True:
#         print(list.pop())
# except IndexError:
#     print(f'All Done - All Elements are popped now')
# print('Code Resumes...')

try:
    while True:
        print(list.pop())
except Exception as ex:
    print(f'Something happened.. {type(ex)}')
print('Code Resumes...')