from time import perf_counter
import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)s: %(message)s',
    level=logging.DEBUG
)
logger = logging.getLogger('Custom Log')


def log(func):
    def inner(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        logger.debug(f'Called {func.__name__}, elapsed={end - start}')
        return result

    return inner


@log
def add(a, b, c):
    return a + b + c


logger.debug(f'Result = {add(1, 2, 3)}')
