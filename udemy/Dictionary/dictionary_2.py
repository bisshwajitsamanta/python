transactions = [
    {'item': 'widget','trans_type':'sale','quantity':7},
{'item': 'widget','trans_type':'sale','quantity':5},
{'item': 'widget','trans_type':'refund','quantity':5},
{'item': 'license','trans_type':'sale','quantity':8},
{'item': 'license','trans_type':'sale','quantity':2},
{'item': 'license','trans_type':'refund','quantity':3}
]

# total_sold ={}
# for transaction in transactions:
#     item = transaction['item']
#     is_sale = transaction['trans_type'] == 'sale'
#     quantity = transaction['quantity']
#
#     if is_sale:
#         total_sold[item] = total_sold.get(item,0)+ quantity
# print(total_sold)

net_sales = {}

for transaction in transactions:
    item = transaction.get('item')
    quantity = transaction.get('quantity')
    is_sale = transaction.get('trans_type') == 'sale'

    if not is_sale:
        quantity = -quantity
    net_sales[item] = net_sales.get(item,0) + quantity
print(net_sales)

