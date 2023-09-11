file_name = "dexuseu.csv"
f = open(file_name)
try:
    for data in f:
        print(data,end="")
finally:
    f.close()