#conda activate pythondata
#pip install nltk
#python -m nltk.downloader popular

#part-of-speech tagging (PoS)

#I	Personal pronoun (PRP)
#enjoy	Verb, non-third person (VBP)
#biking	Verb, gerund, present participle (VBG)
#on	Preposition or subordinating conjunction (IN)
#the	Determiner (DT)
#trails	Noun, plural (NNS)

import nltk
from nltk import word_tokenize
text = word_tokenize("I enjoy biking on the trails")
output = nltk.pos_tag(text)
print(output)


