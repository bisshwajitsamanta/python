def add(a, b, c: int) -> int:
    print(f'Initial Dictionary Namespace:', locals())
    sum_ = a + b + c
    print(f'After sum_ dictionary Namespace', locals())
    return a + b + c


add(1, 2, 3)
