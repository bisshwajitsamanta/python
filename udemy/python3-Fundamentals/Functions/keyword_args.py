def cordinates_to_json(*,latitude, longitude):
    return f'{{"latitude": {latitude}, "longitude":{longitude}}}'


print(cordinates_to_json(latitude=100.3, longitude=120.4))
