def gen_matrix(rows,cols, default_number:int) -> list:
    return [[default_number for j in range(cols)] for i in range(rows)]

print(gen_matrix(4,8,1))
