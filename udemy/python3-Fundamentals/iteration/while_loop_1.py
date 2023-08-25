import time

price = 100

while price >90:
    print(f'Price {price} - still high, waiting for it to come down ...')
    price -=1
    time.sleep(1)
print(f'Good time to buy at this {price}')