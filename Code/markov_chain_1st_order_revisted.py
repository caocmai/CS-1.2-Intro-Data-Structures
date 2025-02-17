from histogram import open_file, histogram
import random

# This is another way which to code out 1st order markov chain
def generate_markov_1st_order(data):
    markov_model = {}

    for i in range(0, len(data)):
        markov_model[data[i]] = {}

    for i in range(0, len(data) - 1):
        if (data[i + 1] in markov_model[data[i]]):
            markov_model[data[i]][data[i + 1]] += 1
        else:
            markov_model[data[i]][data[i + 1]] = 1

    return markov_model

# Only need histogram if wanting to noramlize the markov chain
def normalize_markov_1st_order(markov, histogram):
    for word in markov:
        for next_word in markov[word]:
            markov[word][next_word] = markov[word][next_word] / histogram[word]
    return markov


# This function uses a normalized markov dictionary
def markov_sample(normalize_markov, next_word=None):
    rand_num = random.choice(list(normalize_markov.keys()))
    
    rand_float = random.random()
    print("target", rand_float)
    fence = float(0.0)

    if next_word is None:
        for key, value in normalize_markov[rand_num].items():
            fence += float(value)
            print("fence", fence)
            if fence >= rand_float:
                return key

    elif next_word is not None:
        for key, value in normalize_markov[next_word].items():
            print("value", value)
            fence += float(value)
            print("fence2", fence)
            if fence >= rand_float:
                return key

# This function does not use a normalized markov dictionary 
def markov_sample_histogram(markov, next_word=None):
    rand_num = random.choice(list(markov.keys()))
    # print("random", rand_num)
    # print("target", rand_float)
    fence = int(0)

    if next_word is None:
        total = sum(markov[rand_num].values())
        # print("total", total)
        rand_float = random.randint(1, total)
        # print("float3243", rand_float)
        for key, value in markov[rand_num].items():
            fence += int(value)
            # print("fence", fence)
            if fence >= rand_float:
                return key

    elif next_word is not None:
        total2 = sum(markov[next_word].values())
        # print("total2", total2)
        rand_float2 = random.randint(1, total2)

        for key, value in markov[next_word].items():
            # print("value", value)
            fence += int(value)
            # print("fence2", fence)
            if fence >= rand_float2:
                return key



### Testing(does not use the normalized markov and just uses regular markov chain)
if __name__ == '__main__':
    content = open_file("test.txt")
    marv = generate_markov_1st_order(content)
    print(marv)
    i = 10
    markov_example = markov_sample_histogram(marv)
    sentence = ''

    while i > 0: 
        markov_example2 = markov_sample_histogram(marv, markov_example)
        sentence += " " + markov_example2
        markov_example = markov_example2
        # print(i)
        i -= 1

    print(sentence)