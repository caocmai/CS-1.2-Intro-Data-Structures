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
        created_list = [word, count] # To change to list just use [] instead of ()
        new_list.append(created_list)

    return_list = []
    for word in new_list:
        if word not in return_list:
            return_list.append(word)

    return return_list

print(to_list(open_file()))