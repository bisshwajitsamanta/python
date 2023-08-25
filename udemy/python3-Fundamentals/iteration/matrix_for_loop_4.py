m = [
    [1,2,3,4],
    [5,6,7],
    [8,9,10,11],
    [12]
]
# matrix is a list of list objects
for row_idx in range(len(m)):
    for col_idx in range(len(m[row_idx])):
        print(f'[{row_idx},{col_idx}]= {row_idx},{col_idx}')
    print('-'*10)