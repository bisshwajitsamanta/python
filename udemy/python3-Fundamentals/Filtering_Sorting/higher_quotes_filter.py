"""
    Filter out the records which opens higher than the close
    symbol, open, high, low, close and volume
    Predicate Function gives you True or False values
"""

quotes = [
    ('AACC', 6.05, 6.07, 6.03, 6.05, 65800),
    ('BACC', 4.05, 6.07, 6.03, 16.05, 65800),
    ('CACC', 2.05, 6.07, 6.03, 26.05, 65800),
    ('DACC', 1.05, 6.07, 6.03, 60.05, 65800),
    ('EACC', 8.05, 6.07, 6.03, 6.05, 65800),
]


def close_higher(rec):
    open_ = rec[1]
    close = rec[4]
    return close > open_

print(close_higher(('DACC', 1.05, 6.07, 6.03, 60.05, 65800)))
data = [('DACC', 1.05, 6.07, 6.03, 60.05, 65800)]
# Lambda way

print(f'Filtered Values:{list(filter(lambda rec: rec[4]>rec[1], quotes))}')
