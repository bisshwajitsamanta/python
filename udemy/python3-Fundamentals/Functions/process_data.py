data = [[10,20,30],[100,200,300],[1000,2000,3000]]


def process_data(data, item_sep=',',line_sep='\n'):
    output = ''
    for row in data:
        for col in row:
            output +=output+str(col)+item_sep
        output+=output+line_sep
    return output

print(process_data(data))