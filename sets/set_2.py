s1 = set('abc')
s2 = {True, False}
s3 = {'a',100,200}
s3.add(400)
s3.add(500)
print(s3)
s3.remove(400)
print(s3)
s3.discard(500)
print(s3)
print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))
