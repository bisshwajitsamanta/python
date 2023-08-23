from datetime import datetime


def log(message):
    print(f'{datetime.utcnow().isoformat()}- [{message}]')


def is_all_positive(data: list):
    for element in data:
        if element < 0:
            log('Elements contain Negative Value')
            # return log('Elements contain Negative Value')
            return False
    # log('Elements contain All Positive Value')
    return True


print(is_all_positive([1, 2, 2, -4, 5]))
