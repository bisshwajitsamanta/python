def encrypt(s):
    return ''.join(chr(ord(c)+10) for c in s)
print(encrypt(""))