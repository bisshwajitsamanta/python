from functools import lru_cache


@lru_cache()
def my_func(l):
    return l


print(my_func(2))
print(my_func((2, 3)))
print(my_func("Bisshwajit"))
print(my_func(2.9))
# print(my_func([1,2,3])) ## List, Dictionary and set are un-hashable so lru_cache cannot be applied.
# print(my_func({'a':1,'b':2,'c':3})) # only str, int, float, tuple and NoneType are hashable.
