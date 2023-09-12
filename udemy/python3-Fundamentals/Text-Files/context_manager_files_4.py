file_path = "dexuseu.csv"
data = []
with open(file_path) as f:
    next(f)
    for row in f:
        row = row.strip()
        date, value_str = row.split(',')
        try:
            value = float(value_str)
            data.append((date,value))
        except ValueError:
            pass

print(data)