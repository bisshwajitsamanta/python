data = [[10, 20, 30], [100, 200, 300], [1000, 2000, 3000]]


def process_row(row, item_sep):
    print(f'Items: {item_sep.join(str(i) for i in row)}')
    return item_sep.join(str(i) for i in row)


def process_data(data, item_sep=',', line_sep='\n'):

    row_strings = (process_row(row, item_sep) for row in data)
    return line_sep.join(row_strings)


print(process_data(data))
