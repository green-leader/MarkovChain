import numpy as np
from collections import defaultdict


class MarkovChain:
    """A simple Markov Chain Class"""
    def __init__(self):
        self.word_dict = defaultdict(list)

    def read(self, text):
        """read a text file for corpus information"""
        corpus = open(text, encoding='utf8').read().split()
        pairs = self.make_pairs(corpus)
        for key, value in pairs:
            if value not in self.word_dict[key]:
                self.word_dict[key].append(value)

    def reads(self, text):
        """use supplied string as corpus information"""
        corpus = text.split()
        pairs = self.make_pairs(corpus)
        for key, value in pairs:
            if value not in self.word_dict[key]:
                self.word_dict[key].append(value)

    def make_pairs(self, corpus):
        for i in range(len(corpus)-1):
            yield (corpus[i], corpus[i+1])

    def generate(self, length):
        first_word = None
        while first_word is None or first_word.islower():
            first_word = np.random.choice(list(self.word_dict.keys()))
        chain = [first_word]
        for i in range(length - 1):
            chain.append(np.random.choice(self.word_dict[chain[-1]]))
            if len(self.word_dict[chain[-1]]) == 0:
                break
        return ' '.join(chain)


if __name__ == '__main__':
    test = MarkovChain()
    test.read('speeches.txt')
    test.read('timecube.txt')
    # test.read('sample.txt')
    print(test.generate(30))

    test = None
    test = MarkovChain()
    test.reads('The quick brown fox jumped over the lazy dog')
    print(test.generate(30))
