def outer(a, b):
    sum_ = a + b

    def inner():
        prod = a * b
        print(a, b, sum_, prod)
        return "You just called a closure!"

    return inner


# Outer Function expect 2 variables a,b
func = outer(2, 3)
# inner Function doesn't expect any variable so func() is empty
print(func())
# Another way of calling the outer Function
print(outer(4, 5)())
