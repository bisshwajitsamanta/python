def calculate_value(data_list, divisors_list):
    return [dataum / divisor for divisor in divisors_list for dataum in data_list]


print(f'calculate value: {calculate_value([4, 8, 10, 20], [4, 2, 5, 10])}')
