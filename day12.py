def git_bread():
  with open('input/d12.txt') as f:
    data = [line.strip().split("-") for line in f]
  return data

data = git_bread()

m = {i[0]:[] for i in data}
m.update({i[1]:[] for i in data})
for i in data:
  m[i[0]].append(i[1])
  m[i[1]].append(i[0])
queue = []
print(m)