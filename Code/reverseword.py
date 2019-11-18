
def openfile(text):
    # file_name = text

    content = []
    f = open(text, "r")

    for line in f:
        content.extend(line.split())
    
    return content

print(openfile("test.txt"))

def reverse_word(content):
    reverse = ""
    for word in content[::-1]:
        reverse += word + " "

    return reverse

# opening the file, then storing in a list and then reversing the words in the file
sample = openfile("test.txt")
print(reverse_word(sample))