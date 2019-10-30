# from random import random
import random
from word_frequency import open_file, histogram, frequency, total_words

a = (histogram(open_file()))

# a = {"one": 1, "fish": 4, "two": 1, "blue": 1, "red": 1}


# print(frequency("the", histogram(open_file())))
# print(frequency("of", histogram(open_file())))
# print(total_words(histogram(open_file())))
total_words = total_words(histogram(open_file()))
print(total_words)

new_list = []
i = 1000
while i > 0:
  for key,value in a.items():
    if random.randrange(total_words) < value: # randrange is total words but takes way too long 5 mins
      i -= 1
      new_list.append(key)
  
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
  if word == "of":
    of_count += 1
  if word == "the":
    the_count += 1

print("of count", of_count)
print("the count", the_count)

# print(new_list)