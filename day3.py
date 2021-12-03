def p1():
  with open('input/d3.txt') as f:
    data = [line.strip() for line in f]
    # data = [line.split() for line in f]
  
  xd = []
  for i in range(len(data[0])):
    tlist = []
    for j in data:
      tlist.append(j[i])
    xd.append(tlist)
  a = ""
  for i in xd:
    if i.count("1") > i.count("0"):
      a += "1"
    else:
      a += "0"
  b = ""
  for i in xd:
    if i.count("1") < i.count("0"):
      b += "1"
    else:
      b += "0"
  print(int(a, 2) * int(b, 2))
  
def helper(data):
  xd = []
  for i in range(len(data[0])):
    tlist = []
    for j in data:
      tlist.append(j[i])
    xd.append(tlist)
  return xd
    
def p2():
  with open('input/d3.txt') as f:
    data = [line.strip() for line in f]

  xd = helper(data)
  
  ans = ""
  for i in range(len(data[0])):
    temp = []
    if len(data) == 2:
      if data[0][i] == "0":
        ans = data[1]
        break
      else:
        ans = data[0]
        break
    elif xd[i].count("1") > xd[i].count("0"):
      for j in range(len(data)):
        if data[j][i] == "1":
          temp.append(data[j])
    elif xd[i].count("1") < xd[i].count("0"):
      for j in range(len(data)):
          if data[j][i] == "0":
            temp.append(data[j])
    data = temp
    xd = helper(data)
    
  with open('input/d3.txt') as f:
    data = [line.strip() for line in f]

  xd = helper(data)
  
  a = ""
  for i in range(len(data[0])):
    temp = []
    if len(data) == 2:
      if data[0][i] == "0":
        a = data[0]
        break
      else:
        a = data[1]
        break
    elif xd[i].count("1") < xd[i].count("0"):
      for j in range(len(data)):
        if data[j][i] == "1":
          temp.append(data[j])
    elif xd[i].count("1") > xd[i].count("0"):
      for j in range(len(data)):
          if data[j][i] == "0":
            temp.append(data[j])
    data = temp
    xd = helper(data)
    
  print(int(ans,2) * int(a, 2))
if __name__ == '__main__':
  p1()
  p2()
  