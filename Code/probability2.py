# from random import random
# this way is wayyy to slow but more accurate?
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
    i -= 1
    for key, value in a.items():
        rand_num = random.randrange(100)
        if 0 <= rand_num <= int(value / total_words * 100):
            new_list.append(key)
  
# check
of_count = 0
the_count = 0
for word in new_list:
  if word == "of":
    of_count += 1
  if word == "the":
    the_count += 1

print("of count", of_count)
print("the count", the_count)
