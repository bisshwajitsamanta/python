# Goal = Function Receives a string argument ( defaults to an empty string ) and returns a dictionary with the unique
# words and their frequency

from collections import Counter

data = "This is the first sentence. This is the second sentence. This is not the fourth sentence, it is the third " \
       "sentence."

# data = data.replace(',',' ')
# data = data.replace('.',' ')
# splitted = data.split()
#
# freq = dict(Counter(splitted))
# print(freq)

def word_frequencies(s = ''):
    s = s.replace(',',' ').replace('.',' ')
    words = s.split()
    return dict(Counter(words))
print(word_frequencies(data))


def word_freq_dict(s =''):
    s = s.replace(',', ' ').replace('.', ' ')
    words = s.split()
    freq = {}
    for word in words:
        freq[word] =freq.get(word,0)+1
    return freq

print(word_freq_dict(data))
