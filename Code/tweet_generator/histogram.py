import sys

# file_content = []

# with open("test2.txt", "r") as f_handle:
#     # file_content = f.read().split()
#     for line in f_handle:
#         file_content.extend(line.split())

# Or can write as function
def open_file(text):
  f_handle = open(text, "r")
  file_content = []

  # With help of Genji
  unwanted_punctuations = dict.fromkeys(map(ord, '\n\r“”")(‘’_…:*!-;,.?â€œ'), " ") # Change unwated puncuations to space " " 
  
  for line in f_handle:
    parsed_text = line.translate(str.maketrans(unwanted_punctuations)).lower()
    file_content.extend(parsed_text.split())
  return file_content

def histogram(file_content):
    '''Get histogram with given content as input'''
    histogram = {}
    for word in file_content:
        # histogram[word] = histogram.get(word, 0) + 1
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1
    return histogram

def unique_words(histogram):
    '''Find all the unique words in historgram'''
    num_unique = 0
    for value in histogram.values():
        if value == 1:
            num_unique += 1
    return num_unique

def frequency(word, histogram):
    '''Returns number of occurrences for a given word'''
    for key, value in histogram.items():
        if key == word:
            return value

def max_frequency(histogram):
    '''Returns most common word and number of occurrences'''
    max_word = None
    max_value = 0
    for key,value in histogram.items():
        if value > max_value:
            max_value = value
            max_word = key
    return (max_word, max_value)

def total_words(histogram):
    '''Returns total number of words in content'''
    total = 0
    for value in histogram.values():
        total += value
    return total

# print(file_content)
# print(histogram(open_file()))
# print(unique_words(histogram(open_file())))
# print(frequency("time", histogram(open_file())))
# print(total_words(histogram(open_file())))
# print(max_frequency(histogram(open_file())))

# if __name__ == "__main__":
#     params = sys.argv[1:] 
#     word = str(params[0])
#     print(frequency(word, histogram(open_file())))