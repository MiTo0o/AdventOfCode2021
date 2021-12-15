from doodoo import poop
import isCubed

def git_bread():
  with open('input/d11.txt') as f:
    data = [[int(j) for j in line.strip()] for line in f]
  return data

def get_legal_Positions(i, j, data):
  possible = [[i, j + 1], [i, j - 1], [i - 1, j], [i + 1, j], [i - 1, j - 1], [i - 1, j + 1], [i + 1, j + 1], [i + 1, j - 1]]
  return [k for k in possible if k[0] < len(data) and k[1] < len(data[i]) and k[0] >= 0 and k[1] >= 0]


def blinding(data):
  flag = True
  for i in range(len(data)):
    for j in range(len(data[i])):
      if data[i][j] != 0:
        flag = False
        break
  return flag

def step_change(data):
  queue = []
  flashed = []
  
  for i in range(len(data)):
    for j in range(len(data[i])):
      queue.append([i, j])
      
  while queue:
    i, j = poop(queue)
    data[i][j] += 1
    
    if data[i][j] > 9:
      if [i, j] not in flashed:
        flashed.append([i, j])
        data[i][j] = 0
        
      queue.extend(get_legal_Positions(i, j, data))
        
  for i in flashed:
    data[i[0]][i[1]] = 0
  return len(flashed)
  
def p1(data):
  flash = 0
  for step in range(100):
    flash += step_change(data)
  print(flash)
  
def p2(data):
  step = 0
  while not blinding(data):
    step_change(data)
    step += 1
  print(step)
  
p1(git_bread())
p2(git_bread())


print(isCubed.isCubed(5))