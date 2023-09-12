source_file = "dexuseu.csv"
target_file = "output.csv"

"""
    Format which i am looking for 
    YEAR,MONTH,DAY,DEXUSEU
    2023,09,07,2.099
"""
with open(source_file) as f:
    data = f.readlines()
    del data[0]
    data = [line.strip() for line in data]
    data = [line.split(',') for line in data]
    print(data)