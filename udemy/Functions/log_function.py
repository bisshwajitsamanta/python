from datetime import datetime


def log(message):
    print(f'{datetime.utcnow().isoformat()}- [{message}]')


log('Log -01')
