# study = dusty
# night = thing
# act = cat
# dessert = stressed
# bad credit = debit card
# import random 
# random.seed(20)

word_list = ['tac', 'sdad', 'dkfj', 'debittcard', 'tca','credit card', 'cta', 'act']

to_anagram = ['bad credit']

# length = 1
# for word in range(len(a)):
#   if len(b) < length:
#     rand_index = random.randint(0, len(a) - 1)
#     b.append(a[rand_index])
#     a.remove(a[rand_index])
# print(b)a
word_count = 0
for letter in to_anagram[0]:
  word_count += 1
# print(word_count) 
count = 0
new_list = []

return_anagram = []

for i in range(len(word_list)):
  pass
  for a_letter in word_list[i]:
    pass
    for b_letter in to_anagram[0]:
      if a_letter == b_letter:
        count += 1
        # print(a[i])
        # print(count)
        if count == word_count and word_count == len(word_list[i]):
          return_anagram.append(word_list[i])
  count = 0
    # print("letter of B", letter)

print(return_anagram)