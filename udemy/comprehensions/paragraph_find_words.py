# Goal: Find all the words of length 5 or more

paragraph = """
To be, or not to be--that is the question:
whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune
Or to take arms against a sea of troubles
And by opposing end them. To die, to Sleep--
No more--and by a sleep to say we end 
The heartache, and the thousand natural shocks
That flesh is heir to.

"""

punctuation = ",.!:-\n"

word_list = []

for char in punctuation:
    paragraph = paragraph.replace(char,' ')

print(paragraph)

print('-'*10)

# for value in paragraph.split(' '):
#     if len(value)>5:
#         word_list.append(value)
# print(word_list)

new_word_set = {value.lower() for value in paragraph.split(' ') if len(value)>5}
print(new_word_set)