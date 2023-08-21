strings = "Python is an awesome language"

splitted_list = [i for i in strings.split(' ') if len(i)>=5]
print(splitted_list)