
def p1():
  with open('input/d1.txt') as f:
    data = [int(line) for line in f]
  count = sum([1 for i in range(len(data) - 1) if data[i + 1] > data[i]])
  print(count)
  
def p2():
  with open('input/d1.txt') as f:
    data = [int(line) for line in f]
    
  xd = [data[i] + data[i + 1] + data[i + 2] for i in range(len(data) - 2)]
  count = sum([1 for i in range(len(xd) - 1) if xd[i + 1] > xd[i]])
  print(count)
  
if __name__ == '__main__':
  p1()
  p2()
  
  
# first version
#
# p1
# with open('input/d1.txt') as f:
#     data = [int(line) for line in f]
# count = 0
# prev = data[0]
# for x in data[1:]:
#   if x > prev:
#     count += 1
#   prev = x
# print(count)
#
# p2
# with open('input/d1.txt') as f:
#     data = [int(line) for line in f]
# xd = []
# for i in range(len(data) - 2):
#     xd.append(data[i] + data[i + 1] + data[i + 2])
# 
# count = 0
# prev = xd[0]
# for x in xd[1:]:
#   if x > prev:
#     count += 1
#   prev = x
# print(count)