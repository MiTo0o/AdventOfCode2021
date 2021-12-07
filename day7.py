with open('input/d7.txt') as f:
  data = [line.strip() for line in f]
  x = [int(i) for i in data[0].split(",")]
  smol = float('inf')
  m = {}
  for i in range(max(x)):
    nm = {}
    for k in range(len(x)):
      xd = abs(x[k] - i)
      if xd > 0:
        nm[k] = (xd + 1) / 2 * xd
    if sum(nm.values()) < smol:
      smol = sum(nm.values())
      m = nm 
print(sum(m.values()))