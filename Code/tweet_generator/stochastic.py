# from random import random
import random
from word_frequency import open_file, histogram, frequency, total_words

histogram = (histogram(open_file()))

total_words = total_words(histogram)

# print(total_words)

def stochastic(dic, total_words):
  rand_num = random.randint(1, total_words)
  # print(rand_num)
  total_value = 0
  for key,value in dic.items():
    # if rand_num <= value:
    # print("total_value", total_value)
    if rand_num - value - total_value <= 0:
      return key
    else:
      total_value += value

# print(stochastic(histogram, total_words))

""" THis is the same as the abovaluee """
# def one(dic, total):
#   rand_num = random.randint(1, total)
#   total_value = 0
#   for key,value in dic.items():
#     if rand_num <= total_value:
#       return key
#     else:
#       total_value += value

