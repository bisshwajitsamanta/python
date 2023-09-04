from time import perf_counter
from datetime import datetime

start = perf_counter()
print(f'Timer started at {datetime.now()}')
input("Press 'Enter' to stop the Timer")
end = perf_counter()
print(f'Timer stopped at {end - start}')