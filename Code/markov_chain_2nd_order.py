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
            if tuple(content[i: i + order]) not in self.keys():
                self[tuple(content[i: i + order])] = []
                self.types += 1
            self[tuple(content[i: i + order])].append(tuple(content[i + 1 : i + order + 1]))
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
