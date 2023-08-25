try:
    1/0
except ZeroDivisionError as ex:
    print(f'Exception occurred: {type(ex)}, {ex}')
print('Code Continues Here...')