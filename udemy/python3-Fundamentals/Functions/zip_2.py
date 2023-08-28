from pprint import pprint
data = [
    ('item1',10,100.0),
    ('item2',12,110.0),
    ('item3',14,140.0)
]
schema = ('widget','num_sold','unit_price')
# d = {}
# for items in data:
#     d[items[0]] ={'num_sold': items[1],'unit_price': items[2]}
# pprint.PrettyPrinter(width=10).pprint(d)

data_dict ={}
for el in data:
    data_dict[el[0]]= dict(zip(schema[1:],el[1:]))
print(data_dict)

data2 = [
    ('item1','manu-1',10,100.0,'0.2'),
    ('item2','manu-2',10,100.0,'0.3'),
    ('item3','manu-3',10,100.0,'0.4'),
]

schema1 = ('widget','manufacturer','num_sold','unit_price','discount')
# Dictionary Comprehension
new_data_dict = { el[0]:dict(zip(schema1[1:],el[1:])) for el in data2}
pprint(new_data_dict)