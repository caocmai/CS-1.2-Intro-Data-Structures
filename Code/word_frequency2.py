# this only works if data is perfect


def content():
  content = []
  f_handle = open("test.txt", "r")
  for line in f_handle:
    content.extend(line.split())
  return content

def clean(content):
  new_list = []
  for word in content:
    if word not in new_list:
      new_list.append(word)
  return new_list

def list_count(content, clean):
  list_count = []
  count = 0
  for word in clean:
    for stuff in content:
      if word == stuff:
        count += 1
      else:
        count = 1
    list_count.append(count)
  return list_count

def answer(clean, o_list):
  answer = []
  while len(clean)> 0:
    f = []
    for i in range(len(clean)):
      f.append(clean[0])
      clean.remove(clean[0])
      for thing in range(len(o_list)):
        f.append(o_list[0])
        o_list.remove(o_list[0])
        answer.append(f)
        f=[]
        break
  return answer

content = content()
clean = clean(content)
list_stuff = list_count(content, clean)

print(answer(clean, list_stuff))
