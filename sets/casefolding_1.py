import string

text = 'a quick brown fox jumps over the lazy dog'
alphabets = set(string.ascii_letters) - set(text)
print(list(alphabets))
alphabets = set(string.ascii_letters.casefold()) - set(text.casefold())
print(list(alphabets))