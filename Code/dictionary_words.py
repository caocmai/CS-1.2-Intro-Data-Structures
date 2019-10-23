import random
import sys

file_content = []

with open("/usr/share/dict/words", "r") as f:
    for line in f:
        file_content.append(line)

# print(a)
def random_sentence(words_list, length):
    choosen_words = []

    for _ in range(len(words_list)):
        if len(choosen_words) < length:
            rand_index = random.randint(0, len(words_list) - 1)
            choosen_words.append(words_list[rand_index])
            words_list.remove(words_list[rand_index])    
  
    # Got from stackoverflow: https://stackoverflow.com/questions/52796911/remove-newline-characters-from-a-list
    # This to remove '\n' from list
    choosen_words = list(map(str.strip, choosen_words)) 
    print(" ".join(choosen_words))
    # return (" ".join(choosen_words))

if __name__ == "__main__":
    params = sys.argv[1:]
    number = int(params[0])
    random_sentence(file_content, number)