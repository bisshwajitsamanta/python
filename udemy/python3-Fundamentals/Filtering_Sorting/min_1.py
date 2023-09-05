
data = [
    {'date': '2020-04-09', 'symbol': 'AAPL', 'open': 268.70, 'high': 270.04, 'low': 364.70, 'close': 367.99},
    {'date': '2020-04-09', 'symbol': 'MSFT', 'open': 168.70, 'high': 270.04, 'low': 265.70, 'close': 567.99},
    {'date': '2020-04-09', 'symbol': 'AMZN', 'open': 298.70, 'high': 270.04, 'low': 264.70, 'close': 467.99},
    {'date': '2020-04-09', 'symbol': 'FB', 'open': 2688.70, 'high': 270.04, 'low': 2640.70, 'close': 667.99},
    {'date': '2020-04-09', 'symbol': 'JIO', 'open': 26008.70, 'high': 270.04, 'low': 289084.70, 'close': 2670000.99},
]

print(f'Sorting based on Minimum: {min(data,key=lambda d: d["low"])}')

data2 = [43,4,5]
print(min(data2))