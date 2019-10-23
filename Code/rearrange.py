import random
import sys

def to_random(sentence):
  split_words = sentence.split(" ")
  new = []

  while len(split_words) > 0:
    for _ in range(len(split_words)):
      rand_index = random.randint(0, len(split_words) - 1)
      new.append(split_words[rand_index])
      split_words.remove(split_words[rand_index])
  
#   return (' '.join(new))
  print(' '.join(new))


# print(to_random("what is today's date"))

if __name__ == "__main__":
    sentence = ' '.join(sys.argv[1:])
    to_random(sentence)