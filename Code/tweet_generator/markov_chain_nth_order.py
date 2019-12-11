import sys
from dictogram import Dictogram
from histogram import open_file
import random

class Markov(dict):

    def __init__(self, content=None, order=1):
        
        self.types = 0
        self.order = order
        self.markov_chain(content, order)

    def markov_chain(self, content, order):
        """Creates a markov chain with specified order"""
        for i in range(len(content) - order):
            if tuple(content[i : i + order]) not in self.keys():
                self[tuple(content[i : i + order])] = []
                self.types += 1
            self[tuple(content[i : i + order])].append(tuple(content[i + 1 : i + order + 1]))
        for key in self.keys():
            self[key] = Dictogram(self[key])
        
    def get_sentence(self, length):
        """Get a random sentence with the specified length"""
        start = random.choice(list(self.keys()))
        sentence = list(start)

        for _ in range(length - self.order):
            next_tuple = self[start].sample()
            sentence.append(next_tuple[self.order - 1])
            start = next_tuple

        return ' '.join(sentence)


if __name__ == '__main__':
    # words = open_file("test3.txt")
    words = ['i', 'like', 'cats', 'and', 'you', 'like', 'cats', 'i', 'like', 'dogs', 'but', 'you', 'hate', 'dogs']
    markov_chain_2nd_order = Markov(words, 2)
    assert markov_chain_2nd_order == {
        ('i' , 'like'): {('like', 'cats'): 1, ('like', 'dogs'): 1}, 
        ('like', 'cats'): {('cats', 'and'): 1, ('cats', 'i'): 1},
        ('cats', 'and'): {('and', 'you'): 1},
        ('and', 'you'): {('you', 'like'): 1},
        ('you', 'like'): {('like', 'cats'): 1},
        ('cats', 'i'): {('i', 'like'): 1},
        ('like', 'dogs'): {('dogs', 'but'): 1},
        ('dogs', 'but'): {('but', 'you'): 1},
        ('but', 'you'): {('you', 'hate'): 1},
        ('you' , 'hate'): {('hate', 'dogs'): 1}
        }
    print(markov_chain_2nd_order)
    print(markov_chain_2nd_order.get_sentence(10))