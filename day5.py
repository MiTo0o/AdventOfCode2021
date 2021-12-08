with open('input/d5.txt') as f:
  data = [line.strip().split(" -> ") for line in f]
  parsed = []
  for i in data:
    t = i[0].split(",")
    t2 = i[1].split(",")
    parsed.append([(int(t[0]), int(t[1])), (int(t2[0]), int(t2[1]))])
  # cover = 0
  matrix = []
  for i in range(1000):
    matrix.append([0] * 1000)
  for coord in parsed:
    x1 = coord[0][0]
    y1 = coord[0][1]
    x2 = coord[1][0]
    y2 = coord[1][1]
    if x2 == x1 and y1 == y2:
      matrix[y1][x1] += 1
    else:
      if x2 == x1:
        if y2 > y1:
          for i in range(y1, y2 + 1):
            matrix[i][x1] += 1
        else:
          for i in range(y2, y1 + 1):
            matrix[i][x1] += 1
      elif y2 == y1:
        if x1 > x2:
          for i in range(x2, x1 + 1):
            matrix[y1][i] += 1
        else:
          for i in range(x1, x2 + 1):
            matrix[y1][i] += 1
      elif x1 > x2 and y1 > y2:
        matrix[y1][x1] += 1
        while x1 != x2:
          x1 -= 1
          y1 -= 1
          matrix[y1][x1] += 1
      elif x1 < x2 and y1 < y2:
        matrix[y1][x1] += 1
        while x1 != x2:
          x1 += 1
          y1 += 1
          matrix[y1][x1] += 1
      elif x1 > x2 and y1 < y2:
        matrix[y1][x1] += 1
        while x1 != x2:
          x1 -= 1
          y1 += 1
          matrix[y1][x1] += 1
      elif x1 < x2 and y1 > y2:
        matrix[y1][x1] += 1
        while x1 != x2:
          x1 += 1
          y1 -= 1
          matrix[y1][x1] += 1
          
count = 0
for i in matrix:
  count += len(list(filter(lambda x: x > 1, i)))
print(count)