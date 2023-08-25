def average(*values):
    try:
        return sum(values) / len(values)
    except ZeroDivisionError:
        return 0


print(f'Average: {average(0)}')
