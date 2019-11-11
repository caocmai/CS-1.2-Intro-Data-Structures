# from random import random
import random
from word_frequency import open_file, histogram, frequency, total_words

histogram = (histogram(open_file()))

# histogram = {"one": 1, "fish": 4, "two": 1, "blue": 1, "red": 1}


# print(frequency("the", histogram(open_file())))
# print(frequency("of", histogram(open_file())))
# print(total_words(histogram(open_file())))
total_words = total_words(histogram(open_file()))

print(total_words)

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

""" THis is the same as the abovaluee """
# def one(dic, total):
#   rand_num = random.randint(1, total)
#   total_value = 0
#   for key,value in dic.items():
#     if rand_num <= total_value:
#       return key
#     else:
#       total_value += value


# fish_count = 0
# blue_count = 0
# one_count = 0
# two_count = 0
# for word in new_list:
#   if word == "fish":
#     fish_count += 1
#   if word == "blue":
#     blue_count += 1
#   if word == "one":
#     one_count += 1
#   if word == "two":
#     two_count += 1

# print("fish word", fish_count)
# print("blue word", blue_count)
# print("one word", one_count)
# print("two word", two_count)

of_count = 0
the_count = 0
for word in new_list:
  if word == "fish":
    of_count += 1
  if word == "one":
    the_count += 1

print("fish", of_count)
print("one", the_count)

# print(new_list)