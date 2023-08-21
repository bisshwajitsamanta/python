# Goal is to get the count of duplicate items in a dictionary
data = ['a','a','c','c','a','a','a','a','b','b','c','d','d']
freq = {}
for element in set(data):
    count = len([char for char in data if char == element])
    freq[element]=count
print(freq)

word_frequency = {
    element: len([char for char in data if char == element]) for element in set(data)
}
print(word_frequency)