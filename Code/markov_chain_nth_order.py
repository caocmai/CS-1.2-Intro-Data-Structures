import sys
from dictogram import Dictogram
from histogram import open_file
import random

class Markov(dict):

    def __init__(self, content=None, order=1):
        
        self.order = order
        self.markov_chain(content, order)

    def markov_chain(self, content, order):
        """Creates a markov chain with specified order"""
        for i in range(len(content) - order): # Loop through content minus the order
            if tuple(content[i: i+order]) not in self.keys(): # Markov is a dictionary
                self[tuple(content[i: i+order])] = [] # Set new tuple to be a list, if not in keys

            self[tuple(content[i: i+order])].append(tuple(content[i+1 : i+order+1])) # else append the next word(s) based on the order
        
        for key in self.keys(): 
            self[key] = Dictogram(self[key]) # Dictogram is assiged to self[key]
        
    def get_sentence(self, length):
        """Get a random sentence with the specified length"""
        first_word = random.choice(list(self.keys())) # Get random word
        sentence = list(first_word) # List starts with first word

        for _ in range(length - self.order):
            next_tuple = self[first_word].sample() # Use sample method from Dictogram class to get next
            sentence.append(next_tuple[self.order - 1])
            first_word = next_tuple # To move down the chain

        return ' '.join(sentence)


if __name__ == '__main__':
    # Testing 2nd order markov
    content = open_file("test3.txt")
    # words = ['i', 'went', 'left', 'you', 'went', 'right', 'i','went','left', 'i', 'went', 'right']
    markov_chain_2nd_order = Markov(content, 4)
    # assert markov_chain_2nd_order == {
    #     ('i' , 'like'): {('like', 'cats'): 1, ('like', 'dogs'): 1}, 
    #     ('like', 'cats'): {('cats', 'and'): 1, ('cats', 'i'): 1},
    #     ('cats', 'and'): {('and', 'you'): 1},
    #     ('and', 'you'): {('you', 'like'): 1},
    #     ('you', 'like'): {('like', 'cats'): 1},
    #     ('cats', 'i'): {('i', 'like'): 1},
    #     ('like', 'dogs'): {('dogs', 'but'): 1},
    #     ('dogs', 'but'): {('but', 'you'): 1},
    #     ('but', 'you'): {('you', 'hate'): 1},
    #     ('you' , 'hate'): {('hate', 'dogs'): 1}
    #     }
    print(markov_chain_2nd_order)
    print(markov_chain_2nd_order.get_sentence(10))