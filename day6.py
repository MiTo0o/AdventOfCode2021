with open('input/d6.txt') as f:
  data = [line.strip() for line in f]
  init = {}
  for i in range(9):
    init[str(i)] = 0
  for i in data[0].split(","):
    init[str(i)] += 1
temp = 0
for i in range(256):
  temp_dict = {}
  for k in range(9):
    temp_dict[str(k)] = 0
  for j in init.keys():
    temp = init[j]
    if j == '0':
      temp_dict["8"] += temp
      temp_dict["6"] += temp
    else:
      temp_dict[str(int(j) - 1)] += temp
  init = temp_dict
print(sum(init.values()))