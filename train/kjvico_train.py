import random
import markovify
import re
import spacy

random.seed(random.SystemRandom())

# Load the spaCy English model
nlp = spacy.load("en")

# Replace the word_split and word_join methods in markovify with spaCy models, as shown in the markovify demo
class POSifiedText(markovify.Text):
    def word_split(self, sentence):
        return ["::".join((word.orth_, word.pos_)) for word in nlp(sentence)]

    def word_join(self, words):
        sentence = " ".join(word.split("::")[0] for word in words)
        return sentence

# Load the kjv text
kjv = open("corpus/kjv.txt").read()
kjvmodel = markovify.Text(kjv)

# Load the icos
ico = open("corpus/icos_cleaned.txt").read()
icomodel = markovify.Text(ico)

# Feel free to play with the parameters of the combined model, but 1:1.7 seems to work ok empirically
kjvicomodel = markovify.combine([ kjvmodel, icomodel ], [ 1, 1.7 ])

for i in range(96):
   print(kjvicomodel.make_short_sentence(280))
