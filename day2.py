def p1():
  with open('input/d2.txt') as f:
    data = [line.split() for line in f]
    
  x = 0
  d = 0
  for i in data:
    if i[0] == "forward":
      x += int(i[1])
    elif i[0] == "up":
      d -= int(i[1])
    else:
      d += int(i[1])
      
  print(d * x)
  
def p2():
  with open('input/d2.txt') as f:
    data = [line.split() for line in f]
    
  x = 0
  d = 0
  a = 0
  for i in data:
    if i[0] == "forward":
      x += int(i[1])
      d += a * int(i[1])
    elif i[0] == "up":
      a -= int(i[1])
    else:
      a += int(i[1])
  
  print(x*d)
  
if __name__ == '__main__':
  p1()
  p2()
  