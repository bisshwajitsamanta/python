s1 = set('abcx')
s2 = set('xyzb')
print(s1|s2) #union
print(s1&s2) #intersection
print(s1-s2)

str_1 ="Python is an awesome language"
str_2 = "Python is a snake"

set_1, set_2 = set(str_1), set(str_2)
print(list(set_1 &set_2))

a1 = {'FB','AMZN','AAPL','NFLX','GOOG','MSFT'}
a2 = {'BABA','WMT','COST','NFLX','GOOG','MSFT'}
a3 = {'F','TSLA','GM','NFLX','GOOG','MSFT'}
print(list(a1|a2|a3))

# Assume a shop is counting what items are sold and what items are returned, so we have 2 lists now we need to find out
# which items got sold but got returned too.

sold = {'s1','s2','s3'}
returned = {'s1'}
non_returned = sold - returned
print(list(non_returned))


# Determine which characters in one string is not present in another string.
alphabets = set('abcdefghijklmnopqrstuvwxyz')