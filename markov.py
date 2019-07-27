import numpy as np
from collections import defaultdict


class MarkovChain:
    """A simple Markov Chain Class"""
    def __init__(self):
        self.word_dict = defaultdict(list)

    def read(self, text):
        corpus = open(text, encoding='utf8').read().split()
        pairs = self.make_pairs(corpus)
        for key, value in pairs:
            self.word_dict[key].append(value)

    def make_pairs(self, corpus):
        for i in range(len(corpus)-1):
            yield (corpus[i], corpus[i+1])

    def generate(self, length):
        first_word = None
        while first_word is None or first_word.islower():
            first_word = np.random.choice(list(self.word_dict.keys()))
        chain = [first_word]
        for i in range(length):
            chain.append(np.random.choice(self.word_dict[chain[-1]]))
        return ' '.join(chain)


test = MarkovChain()
test.read('speeches.txt')
test.read('timecube.txt')
print(test.generate(30))
