import sys
from dictogram import Dictogram
from histogram import open_file
import random

class Markov(dict):

    def __init__(self, content=None, order=1):
        
        self.types = 0
        # self.tokens = 1
        self.order = order
        self.markov_chain(content, order)

    def markov_chain(self, content, order):

        for i in range(len(content) - order):
            if tuple(content[i: i + order]) not in self.keys():
                self[tuple(content[i: i + order])] = []
                self.types += 1
            self[tuple(content[i: i + order])].append(tuple(content[i + 1 : i + order + 1]))
            # self.tokens += 1
        for key in self.keys():
            self[key] = Dictogram(self[key])
        
