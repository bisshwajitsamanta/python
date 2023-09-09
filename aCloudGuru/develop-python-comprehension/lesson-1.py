def process_incoming_data(data_list):
    return [(dataum // 2 * 67 - 5) for dataum in data_list]


if __name__ == "__main__":
    data_list = [0, 5, 10, 15]
    print(process_incoming_data(data_list))
