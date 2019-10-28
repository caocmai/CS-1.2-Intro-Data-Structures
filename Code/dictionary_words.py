import random
import sys

file_content = []

with open("/usr/share/dict/words", "r") as f:
    # file_content = f.read().split()
    for line in f:
        file_content.append(line.strip())


"""List comprehension - to create new list from previous list"""
# clean_lines = []
# for line in lines:
#     clean_lines.append(line.strip())

# clean_line = [line.strip() for line in lines]

# Both are the same
# randrange(len(something))
# same as randint(0, len(word)-1)


def random_sentence(words_list, length):
    choosen_words = []

    for _ in range(length):
        rand_index = random.randint(0, len(words_list) - 1)
        choosen_words.append(words_list[rand_index])
        words_list.remove(words_list[rand_index])    
  
    # Got from stackoverflow: https://stackoverflow.com/questions/52796911/remove-newline-characters-from-a-list
    # This to remove '\n' from list: 
    # choosen_words = list(map(str.strip, choosen_words)) 
    print(" ".join(choosen_words))
    # return (" ".join(choosen_words))

if __name__ == "__main__":
    params = sys.argv[1:] 
    number = int(params[0])
    if number < 2:
        print("Not enough for sentence")
    elif number == None:
        print("not correct")
    else:
        random_sentence(file_content, number)