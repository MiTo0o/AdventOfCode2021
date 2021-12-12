with open('input/d11.txt') as f:
  data = [[int(j) for j in line.strip()] for line in f]

  flashes = 0
  for step in range(100):
    queue = []
    flashed = []
    for i in range(len(data)):
      for j in range(len(data[i])):
        queue.append([i, j])
    while len(queue) > 0:
      i ,j = queue.pop(0)
      data[i][j] += 1
      
      pos = [[i, j + 1], [i, j - 1], [i - 1, j], [i + 1, j], [i - 1, j - 1], [i - 1, j + 1], [i + 1, j + 1], [i + 1, j - 1]]
      adj = [k for k in pos if k[0] < len(data) and k[1] < len(data[i]) and k[0] >= 0 and k[1] >= 0]

      if data[i][j] > 9:
        if [i, j] not in flashed:
          flashed.append([i, j])
          flashes += 1
          data[i][j] = 0
        for k in adj:
          queue.append(k)
    for i in flashed:
      data[i[0]][i[1]] = 0
  print(flashes)
  
with open('input/d11.txt') as f:
  data = [[int(j) for j in line.strip()] for line in f]

step = 0
while True:
  queue = []
  flashed = []
  for i in range(len(data)):
    for j in range(len(data[i])):
      queue.append([i, j])
  while len(queue) > 0:
    i ,j = queue.pop(0)
    data[i][j] += 1
    
    possible = [[i, j + 1], [i, j - 1], [i - 1, j], [i + 1, j], [i - 1, j - 1], [i - 1, j + 1], [i + 1, j + 1], [i + 1, j - 1]]
    adj = [k for k in possible if k[0] < len(data) and k[1] < len(data[i]) and k[0] >= 0 and k[1] >= 0]

    if data[i][j] > 9:
      if [i, j] not in flashed:
        flashed.append([i, j])
        data[i][j] = 0
      for k in adj:
        queue.append(k)
  for i in flashed:
    data[i[0]][i[1]] = 0
  step += 1
  flag = True
  for i in range(len(data)):
    for j in range(len(data[i])):
      if data[i][j] != 0:
        flag = False
        break
  if flag:
    print(step)
    break