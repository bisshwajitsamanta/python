f = open("/Users/bisshwajitsamanta/code/python/python/aCloudGuru/python-admin-scripting/general.txt")
try:
    print(f.read())
except ValueError:
    print(f'Value error raised')
    raise ValueError
finally:
    print('File is closed now !!')
    f.close()
