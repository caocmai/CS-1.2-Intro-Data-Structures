''' Only works well with a small amount of text '''


def open_file():
    content = []
    f_handle = open("test.txt", "r")
    for line in f_handle:
        content.extend(line.split())
    return content

def find_feq(content):
    new_list = []
    count = 0
    for word in content:
        for word_2 in content: # Instead of using the count(), manually find count
            if word == word_2: 
                count += 1
            else:
                pass
        new_tuple = (word, count)
        new_list.append(new_tuple)
        count = 0

    clean_list = []
    for item in new_list:
        if item not in clean_list:
            clean_list.append(item)
        else:
            pass
    return clean_list

print(find_feq(open_file()))
# print(open_file())