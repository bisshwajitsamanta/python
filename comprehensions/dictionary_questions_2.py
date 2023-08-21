not_divisible = []
for i in range(1, 101):
    for j in range(2, 9):
        if i % j == 0:
            not_divisible.append(i)

missing_elements = []
for element in range(1,101):
    for present in not_divisible:
        if element not in not_divisible:
            missing_elements.append(element)

print(set(missing_elements))

not_divise = [ [ i for j in range(2,9) if i %j ==0] for i in range(1,101)]
missed = [[e for present in not_divise if e not in not_divise]for e in range(1,101)]
print(set(missed))