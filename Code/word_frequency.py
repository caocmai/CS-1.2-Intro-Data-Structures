file_content = []

with open("test.txt", "r") as f:
    # file_content = f.read().split()
    for line in f:
        file_content.append(line.strip())

def histogram(file_content):
    histogram = {}
    for word in file_content:
        # histogram[word] = histogram.get(word, 0) + 1
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1
    return histogram

def unique_words(histogram):
    num_unique = 0
    for value in histogram.values():
        if value == 1:
            num_unique += 1
    return num_unique

def frequency(word, histogram):
    for key, value in histogram.items():
        if key == word:
            return value


# print(file_content)
print(histogram(file_content))
# print(unique_words(histogram(file_content)))
# print(frequency("value", histogram(file_content)))