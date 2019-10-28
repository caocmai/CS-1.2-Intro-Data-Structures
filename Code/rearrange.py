import random
import sys

def rearrange(sentence):
  split_words = sentence.split(" ")
  new_sentence = []

  while len(split_words) > 0:
    for _ in range(len(split_words)):
      rand_index = random.randint(0, len(split_words) - 1)
      new_sentence.append(split_words[rand_index])
      split_words.remove(split_words[rand_index])
  
#   return (' '.join(new_sentence))
  print(' '.join(new_sentence))
  # print(new_sentence)

if __name__ == "__main__":
    sentence = " ".join(sys.argv[1:])
    rearrange(sentence)