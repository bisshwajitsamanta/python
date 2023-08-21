# Create a dictionary whose keys are the widget names and the values the number of sales but only include widgets
# that had sales
widgets = ['widget1','widget2','widget3','widget4','widget5']
sales = [10,5,3,9,0]

only_sales = {}
for item in range(len(widgets)):
    if sales[item]>0:
        only_sales[widgets[item]]=sales[item]
        print(only_sales)
print(only_sales)


no_zero_sales = {widgets[i]:sales[i] for i in range(len(widgets)) if sales[i]>0}
print(no_zero_sales)