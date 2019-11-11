''' Only works well with a small amount of text '''

def open_file():
    content = []
    f_handle = open("test3.txt", "r")
    for line in f_handle:
        content.extend(line.split())
    return content

# print(open_file())

# Can change to tuple or list with a change to line 15
def to_list(content):
    new_list = []
    for word in content:
        count = content.count(word)
        temp_list = [word, count] # To change to list just use [] instead of ()
        new_list.append(temp_list)

    return_list = []
    for word in new_list:
        if word not in return_list:
            return_list.append(word)

    return return_list

print(to_list(open_file()))

#for list
def to_list(content):
    list_histo = []
    for c_word in content:
        exists = False
        for word in list_histo:
            if word[0] == c_word:
                word[1] += 1
                exists = True
        if exists == False:
            list_histo.append([word, 1])
    return list_histo

# to tuple 
def to_tuple(content):
    to_tupe = []
    amount = 0
    for word in text:
        is_updated = False
        for tuple in histogram:
            if tuple[0] == word:
                amount = tuple[1] + 1
                histogram.remove(tuple)
                histogram.append((word, amount))
                is_updated = True
        if is_updated == False:
            histogram.append((word, 1))
    return histogram