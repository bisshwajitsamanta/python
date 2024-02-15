# file_name = "file1.csv"
# with open(file_name) as f:
#     for _ in range(5):
#         print(next(f))

# import csv
# with open("file1.csv") as f:
#     reader = csv.reader(f)
#     print(f'Header: {next(reader)}')
#     data = list(reader)
#     print(f'Rest data: {data}')

import csv
from datetime import datetime
from decimal import Decimal


class Datapoint:
    def __init__(self, date, value):
        # self.date = date
        self.date = datetime.strptime(date, "%Y-%m-%d").date()
        self.value = Decimal(value)


class Forex:
    def __init__(self, file_name):
        self.header = None
        self.file_name = file_name
        self.data = self.process_date()

    def process_date(self):
        with open(self.file_name) as f:
            reader = csv.reader(f)
            self.header = next(reader)
            return [
                Datapoint(date, value)
                for date, value in reader
                if date != '.'
            ]


forex = Forex("file1.csv")
print(forex.header)
print(forex.data[0].date)
print(forex.data[0].value)
