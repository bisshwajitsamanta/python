num = 1234
# value = sorted(str(num),reverse=True)
# stringList= ''.join(value)
stringList= ''.join(sorted(str(num),reverse=True))
newString = str(num)[::-1]
print(stringList)
print(newString)