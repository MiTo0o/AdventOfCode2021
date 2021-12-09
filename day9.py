with open('input/d9.txt') as f:
  cave = [list(line.strip()) for line in f]
# part 1
risk_level = 0
for i in range(len(cave)):
  for j in range(len(cave[i])):
    adjacent_coords = [[i, j + 1], [i, j - 1], [i - 1, j], [i + 1, j]]
    possible_coords = [k for k in adjacent_coords if k[0] < len(cave) and k[1] < len(cave[i]) and k[0] >= 0 and k[1] >= 0]
    if all([cave[k[0]][k[1]] > cave[i][j] for k in possible_coords]):
      risk_level += int(cave[i][j]) + 1
print(risk_level)

# Part 2 (modifies cave array)
def helper(cave, i, j, basin_size):
  if cave[i][j] == "9":
    return
  cave[i][j] = "9"
  basin_size[0] += 1
  if i + 1 < len(cave):
    helper(cave, i + 1, j, basin_size)
  if i - 1 >= 0:
    helper(cave, i - 1, j, basin_size)
  if j + 1 < len(cave[i]):
    helper(cave, i, j + 1, basin_size)
  if j - 1 >= 0:
    helper(cave, i, j - 1, basin_size)

all_basins = []
for i in range(len(cave)):
  for j in range(len(cave[i])):
    if cave[i][j] != "9":
      basin_size = [0]
      helper(cave, i, j, basin_size)
      all_basins.append(basin_size[0])
all_basins.sort()
print(all_basins[-1] * all_basins[-2] * all_basins[-3])