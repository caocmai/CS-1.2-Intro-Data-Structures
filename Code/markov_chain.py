import random

corpus = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']

def make_pairs(corpus):
    for i in range(len(corpus) - 1):
        yield (corpus[i], corpus[i + 1])

pairs = make_pairs(corpus)

word_dict = {}
for word_1, word_2 in pairs:
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1] = [word_2]

first_word = random.choice(corpus)
# while first_word.islower():
chain = [first_word]

n_words = 20
for i in range(n_words): 
    chain.append(random.choice(word_dict[chain[-1]]))


print(' '.join(chain))
