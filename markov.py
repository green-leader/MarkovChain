import numpy as np
from collections import defaultdict
import json


class MarkovChain:
    """A simple Markov Chain Class"""
    def __init__(self):
        self.word_dict = defaultdict(list)

    def read(self, text):
        """read a text file for corpus information"""
        corpus = open(text, encoding='utf8').read().strip().split()
        pairs = self.make_pairs(corpus)
        for key, value in pairs:
            if value not in self.word_dict[key]:
                self.word_dict[key].append(value)
        # print(self.word_dict)

    def reads(self, text):
        """use supplied string as corpus information"""
        corpus = text.strip().split()
        pairs = self.make_pairs(corpus)
        for key, value in pairs:
            if value not in self.word_dict[key]:
                self.word_dict[key].append(value)
        # print(self.word_dict)

    def make_pairs(self, corpus):
        for i in range(len(corpus)-1):
            yield (corpus[i], corpus[i+1])

    def load(self, filename):
        """Load corpus direct from json encoded file"""
        with open(filename, 'r') as f:
            self.word_dict = defaultdict(list, dict(json.load(f)))

    def loads(self, text):
        """Load corpus as json encoded string"""
        self.word_dict = defaultdict(list, dict(json.loads(text)))

    def dump(self, filename):
        """Dump corpus to json encoded file"""
        with open(filename, 'w') as out:
            json.dump(self.word_dict, out)

    def dumps(self):
        """Dump corpus to json encoded string"""
        return json.dumps(self.word_dict)

    def generate(self, length):
        first_word = None
        while first_word is None or first_word.islower():
            first_word = np.random.choice(list(self.word_dict.keys()))
        chain = [first_word]
        for i in range(length - 1):
            chain.append(np.random.choice(self.word_dict[chain[-1]]))
            if chain[-1] not in self.word_dict:
                break
        return ' '.join(chain)


if __name__ == '__main__':

    test = MarkovChain()
    test.reads('The quick brown fox jumped over the lazy dog')
    assert test.generate(30) == test.generate(9)

    fileread = MarkovChain()
    fileread.read('sample.txt')
    assert fileread.word_dict == test.word_dict, \
        ("Value Mismatch: %s != %s" % (fileread.word_dict, test.word_dict))

    # test if dumping then reloading strings results in same output
    second = MarkovChain()
    second.loads(test.dumps())
    assert second.word_dict == test.word_dict

    # test file loading
    third = MarkovChain()
    third.read('sample.txt')
    assert third.word_dict == test.word_dict, (third.word_dict, test.word_dict)

    # test file dump and file load
    third.dump('simple.json')
    fourth = MarkovChain()
    fourth.load('simple.json')
    assert third.word_dict == fourth.word_dict, \
        ("Value Mismatch: %s != %s" % (third.word_dict, fourth.word_dict))
