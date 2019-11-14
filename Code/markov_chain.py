fish_words = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']

histogram = {}

for word in range(len(fish_words) - 1):
    if fish_words[word] not in histogram:
        histogram[fish_words[word]] = {}

print(histogram)

for index in range(len(fish_words) - 1):
    if fish_words[index] in histogram:
        histogram[fish_words[index]][fish_words[index + 1]] = 1
    
    for key in histogram[fish_words[index + 1]].keys():
        if key == fish_words[index]:
            histogram[fish_words[index]][fish_words[index + 1]] += 1

print(histogram)