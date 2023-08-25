given_string = "postgres://u1kuv487bfn47d:p208e0884d22ff9b4d479438c5ef56f8edf25ba719327a8f975ff4731182b6557@ec2-3-72-126-52.eu-central-1.compute.amazonaws.com:5432/d1ad3rf3g79f1p"
first_split =given_string.split(':')
second_split = first_split[2].split('@')
print(second_split[0])
