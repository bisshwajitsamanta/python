# Goal is to create a dictionary with items and sales count
widget_sales = [
    {'name': 'widget1','sales':10},
    {'name': 'widget2','sales':1},
    {'name': 'widget3','sales':9},
]

sales_by_widget ={}
for l in widget_sales:
    widget_name = l['name']
    sales = l['sales']
    sales_by_widget[widget_name] = sales
print(sales_by_widget)
print('-'*10)


sales_by_widget_comprehension = {d['name']:d['sales'] for d in widget_sales if d['sales'] >1}
print(sales_by_widget_comprehension)