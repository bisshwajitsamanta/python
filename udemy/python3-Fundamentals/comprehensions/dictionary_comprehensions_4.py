sales = {
    'widget1': 0,
    'widget2': 1,
    'widget3': 20,
    'widget4':5,
    'widget5':7
}
high_sales = [k for k,v in sales.items() if v >=5]
print(high_sales)