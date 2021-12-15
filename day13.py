import copy
def git_bread():
  with open('input/d13.txt') as f:
    dots = []
    folds = []
    time_for_sum_folds = False
    for line in [i.strip() for i in f]:
      if not line:
        time_for_sum_folds = True
        continue
      if time_for_sum_folds:
        folds.append(line.strip().split()[2])
      else:
        dots.append(list(map(int, line.strip().split(","))))
        
  w = int(max(dots, key=lambda x:x[0])[0]) + 1
  l = int(max(dots, key=lambda x:x[1])[1]) + 1
  
  matrix = [["-" for x in range(w)] for y in range(l)]
  
  for i in dots:
    matrix[i[1]][i[0]] = "@"
    
  return (matrix, folds)
    
def fold(matrix, folds):
  for i in folds:
    tt = int(i.split("=")[1])
    if i[0] == "x":
      for j in range(len(matrix)):
        for k in range(tt + 1, tt * 2 + 1):
          if matrix[j][k] == "@":
            mirror_index = tt * 2 - k
            matrix[j][mirror_index] = "@"
      matrix = [s[:tt] for s in matrix]
    else:
      for j in range(tt + 1, tt * 2 + 1):
        for k in range(len(matrix[j])):
          if matrix[j][k] == "@":
            mirror_index = tt * 2 - j
            matrix[mirror_index][k] = "@"
      matrix = copy.deepcopy(matrix[:tt])
  return matrix

def p1():
  matrix, folds = git_bread()
  folded_matrix = fold(matrix, [folds[0]])
  count = sum([1 for i in folded_matrix for j in i if j == "@"])
  print(count)

def p2():
  matrix, folds = git_bread()
  folded_matrix = fold(matrix, folds)
  for xd in folded_matrix:
    print("".join(xd))
    
p1()
p2()