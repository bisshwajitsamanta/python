for i in range(1,5):
    for j in range(1,5):
        if (i+j) %2 ==1:
            print(f'{i}+{j} is odd skipping ...')
            continue
        print(f'{i}+{j} equals {i+j}')
    print('-'*10)