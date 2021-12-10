import copy
with open('input/d10.txt') as f:
  data = [line.strip() for line in f]
xd = copy.deepcopy(data)
x = {"}":"{", "]":"[",")":"(",">":"<"}
y = {"}":0, "]":0, ")":0, ">":0}
z = {"{":"}", "[":"]","(":")","<":">"}

for i in range(len(data)):
  stack = []
  for j in data[i]:
    if j in x.values():
      stack.append(j)
    else:
      if stack[-1] == x[j]:
        stack.pop()
      else:
        xd[i] = ""
        y[j] += 1
        break
      
# part 2
while not all(i for i in xd if i == ""):
  for j in range(len(xd)):
    if xd[j] == "":
      del xd[j]
      break
scores = []
s = {"}":3, "]":2, ")":1, ">":4}
for i in xd:
  stack = []
  for j in i:
    if j in x.values():
      stack.append(j)
    else:
      if stack[-1] == x[j]:
        stack.pop()
  temp = []
  for j in stack:
    temp.append(z[j])
  tot = 0
  for j in temp[::-1]:
    tot *= 5
    tot += s[j]
  scores.append(tot)
  
scores.sort()
p1_answer = y[")"] * 3 + y["]"] * 57 + y["}"] * 1197 + y[">"] * 25137
print(f"part 1: {p1_answer}")
print(f"part 2: {scores[len(scores)//2]}")