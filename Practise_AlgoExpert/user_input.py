stringList,numList =[],[]

for i in range(5):
    value = input("Enter a String:")
    stringList.append(value)

for i in range(3):
    num = int(input("Enter a number:"))
    numList.append(num)

# Logic to access the list with these numbers
for value in numList:
    print(stringList[value],end="")

