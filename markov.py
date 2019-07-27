import numpy as np
from collections import defaultdict

corpus = open('speeches.txt', encoding='utf8').read().split()


def make_pairs(corpus):
    for i in range(len(corpus)-1):
        yield (corpus[i], corpus[i+1])


pairs = make_pairs(corpus)


word_dict = defaultdict(list)
for key, value in pairs:
    word_dict[key].append(value)

first_word = np.random.choice(corpus)

chain = [first_word]

n_words = 30

for i in range(n_words):
    chain.append(np.random.choice(word_dict[chain[-1]]))

print(' '.join(chain))
