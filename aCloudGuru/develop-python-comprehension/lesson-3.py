def find_usable_data(data_list):
    return [dataum if dataum > 90 and dataum % 2 == 0 else -100 for dataum in data_list]


print(f'Data List:{find_usable_data([100, 15, 78, 35])}')
