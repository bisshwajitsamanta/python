# You are given a list of lists containing two numbers that will need to be color coded later based on a trend
# determined by the following rules: 1. If the first number of a row is higher than the second number of the previous
# row, append the string `up` to the row 2. If the first number of a row is lower than the second number of the
# previous row, append the string `down` to the row 3. Otherwise, append `same` to the row.
#
# Obviously you cannot apply these rules to the first row (there is no preceding row), so append an empty string for
# the first row.
#
# Basically think of this as a list of Open/Close values, and we want to assign the values `same`, `up`,
# or `down` based on how a row's Open value compares to the Close of the *previous* row.


data = [
    [10, 20],
    [20, 30],
    [35, 50],
    [45, 60]
]

for index, i in enumerate(data):
    print(i)
# i[1]