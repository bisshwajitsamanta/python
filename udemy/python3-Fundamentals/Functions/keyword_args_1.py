# {"arg1":10,"kw1":=20,"extras":{a:1,b:2,c:3}}
def to_json(arg1, *, kw1, **extras):
    # formatted_string= ','.join(f'{k}:{v}' for k, v in extras.items())
    formatted_string = ','.join(f'{k}:{v}' for k, v in extras.items())
    return f'{{"args": {arg1},"kw1":{kw1},"extras":{formatted_string}}}'


print(to_json(10, kw1=20, a=3, b=23, c=45))
