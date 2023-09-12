file_name = "dexuseu.csv"

with open(file_name) as f:
    # print(f.readlines()) # This takes all the file in memory
    next(f)
    for row in f:
        row = row.strip()
        date, value_str = row.split(',')
        print(date, value_str)