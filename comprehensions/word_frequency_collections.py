from collections import Counter

data = ['a','a','c','c','a','a','a','a','b','b','c','d','d']
freq = Counter(data)
print(dict(freq))

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

punctuation = " ,\n-':"

new_dict ={k:v for k,v in Counter(paragraph.casefold()).items() if k not in punctuation}
print(new_dict)