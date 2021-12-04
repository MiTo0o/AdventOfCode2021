def p1():
  with open('input/d4.txt') as f:
    data = [line.strip() for line in f]
    boards = []
    temp = []
    for i in data[2:]:
      if i != "":
        temp.append(i.split())
      else:
        boards.append(temp)
        temp = []
    boards.append(temp)

  ip = [85,84,30,15,46,71,64,45,13,90,63,89,62,25,87,68,73,47,65,78,2,27,67,95,88,99,96,17,42,31,91,98,57,28,38,93,43,0,55,49,22,24,82,54,59,52,3,26,9,32,4,48,39,50,80,21,5,1,23,10,58,34,12,35,74,8,6,79,40,76,86,69,81,61,14,92,97,19,7,51,33,11,77,75,20,70,29,36,60,18,56,37,72,41,94,44,83,66,16,53]
  for i in ip:
    w = False
    for j in boards:
      if won(j):
        w = True
        c = 0
        for k in range(5):
          for x in range(5):
            if j[k][x] != '-':
              c += int(j[k][x])
        print(c * i)
        break
    if w:
      break
    
    for j in boards:
      for k in range(5):
        for x in range(5):
          if j[k][x] == str(i):
            j[k][x] = "-"
    for j in boards:
      if won(j):
        w = True
        c = 0
        for k in range(5):
          for x in range(5):
            if j[k][x] != '-':
              c += int(j[k][x])
        print(c * i)
        break
    if w:
      break
  
def won(b):
  for i in b:
    if i.count("-") == 5:
      return True
  flipped = []
  for i in range(5):
    temp = []
    for j in range(5):
      temp.append(b[j][i])
    flipped.append(temp)
  for i in flipped:
    if i.count("-") == 5:
      return True
    
  return False

def p2():
  with open('input/d4.txt') as f:
    data = [line.strip() for line in f]
    boards = []
    temp = []
    for i in data[2:]:
      if i != "":
        temp.append(i.split())
      else:
        boards.append(temp)
        temp = []
    boards.append(temp)
  xd = 0
  ip = [85,84,30,15,46,71,64,45,13,90,63,89,62,25,87,68,73,47,65,78,2,27,67,95,88,99,96,17,42,31,91,98,57,28,38,93,43,0,55,49,22,24,82,54,59,52,3,26,9,32,4,48,39,50,80,21,5,1,23,10,58,34,12,35,74,8,6,79,40,76,86,69,81,61,14,92,97,19,7,51,33,11,77,75,20,70,29,36,60,18,56,37,72,41,94,44,83,66,16,53
]
  
  for i in ip:
    for j in boards:
      for k in range(5):
        for x in range(5):
          if j[k][x] == str(i):
            j[k][x] = "-"
    index = 0
    while index < len(boards):
      if won(boards[index]):
        if len(boards) > 1:
          del boards[index]
          # index -= 1
        else:
          index += 1
      else:
        index += 1
    if len(boards) == 1:
      if won(boards[0]):
        xd = i
        break
  c = 0
  for k in range(5):
    for x in range(5):
      if boards[0][k][x] != '-':
        c += int(boards[0][k][x])
  print(c * xd)
if __name__ == '__main__':
  p1()
  p2()
  