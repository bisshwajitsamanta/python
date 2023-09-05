data = [-10,-6,0,3,6]
def key_func(x):
    return abs(x)

print(sorted(data,key=key_func))

data1=[5,2,20,-2,1,-1]
print(f'Sorted Data:{sorted(data1,key=abs,reverse=False)}')
