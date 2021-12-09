
with open('input/d9.txt') as f:
  data = [line.strip() for line in f]
  for i in range(len(data)):
    data[i] = list(data[i])

def helper(grid, i, j, temp):
  if grid[i][j] == "9":
      return
  grid[i][j] = "9"
  temp[0] += 1
  if i + 1 < len(grid):
      helper(grid, i + 1, j, temp)
  if i - 1 >= 0:
      helper(grid, i - 1, j, temp)
  if j + 1 < len(grid[i]):
      helper(grid, i, j + 1, temp)
  if j - 1 >= 0:
      helper(grid, i, j - 1, temp)

s = []
for i in range(len(data)):
  for j in range(len(data[i])):
    if data[i][j] != "9":
      temp = [0]
      helper(data, i, j, temp)
      s.append(temp[0])
s.sort()
print(s[-1] * s[-2] * s[-3])






















# part 1

# with open('input/d9.txt') as f:
#   data = [line.strip() for line in f]
#   s = 0
#   print(data)
#   for i in range(len(data)):
#     # print(data[i])
#     for j in range(len(data[i])):
#       combo = [[i, j + 1], [i, j - 1], [i - 1, j], [i + 1, j]]
#       possible = [k for k in combo if k[0] < len(data) and k[1] < len(data[i]) and k[0] > -1 and k[1] > -1]
#       flag = True
#       for k in possible:

#         if data[k[0]][k[1]] <= data[i][j]:
#           flag = False
#       if flag:
#         print(i, j)
#         print(data[i][j])
#         s += int(data[i][j]) + 1

#     # for j in range(len(i)):
#     #   if j == len(i) - 1:
#     #     if int(i[j]) < int(i[j - 1]):
#     #       s += int(i[j]) + 1
#     #   elif j == 0:
#     #     if int(i[j]) < int(i[j + 1]):
#     #       s += int(i[j]) + 1
#     #   else:
#     #     if int(i[j]) < int(i[j + 1]) and int(i[j - 1]):
#     #       s += int(i[j]) + 1
#   print(s)

















