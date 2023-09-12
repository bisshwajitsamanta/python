file_path = "dexuseu.csv"

with open(file_path) as f:
    for _ in range(3):
        print(next(f).strip())

    # for line in f:
    #     print(line,end="")
