# m = [
#     [0,1,2],
#     [3,4,5,6,7],
#     [8,9,10],
#     [11]
# ]
m = [[0,1,2],[3,4,5,6,7],[8,9,10],[11]]

for row_idx, row in enumerate(m):
    for col_idx, elements in enumerate(row):
        print(f'[{row_idx},{col_idx}]={elements}')
