import copy
def git_bread():
  with open('input/d14.txt') as f:
    data = [line.strip().split(" -> ") for line in f]
  return data

current = "KHSNHFKVVSVPSCVHBHNP"
data = git_bread()

pair = [i[0] for i in data]
insert = [i[1] for i in data]
# print(pair)

for i in range(10):
  temp = ""
  all_pairs = [current[j] + current[j + 1] for j in range(len(current) - 1) ]
  for j in range(len(all_pairs)):
    if j != len(all_pairs) - 1:
      tt = pair.index(all_pairs[j])
      temp += all_pairs[j][0] + insert[tt]
    else:

      tt = pair.index(all_pairs[j])
      temp += all_pairs[j][0] + insert[tt] + all_pairs[j][1]
  print(i)
  current = temp

# print(len(current))
print(current.count(max(set(current), key = current.count)) - current.count(min(set(current), key = current.count)))

print(max(set(current), key = current.count))
print(min(set(current), key = current.count))

# NBBBCNCCNBBNBNBBCHBBHHBCHB
# NBBBCNCCNBBNBNBBCHBHHBCHB
# NBBBCNCCNBBNBNBBCHBHHBCHB

# print("NBCCNBBBCBHCB" == "NBCCNBBBCBHCB")



# import copy
# def git_bread():
#   with open('input/d14.txt') as f:
#     data = [line.strip().split(" -> ") for line in f]
#   return data

# current = "KHSNHFKVVSVPSCVHBHNP"
# data = git_bread()

# pair = [i[0] for i in data]
# insert = [i[1] for i in data]
# # print(pair)

# for i in range(40):
#   temp = ""
#   all_pairs = [current[j] + current[j + 1] for j in range(len(current) - 1) ]
#   for j in range(len(all_pairs)):
#     if j != len(all_pairs) - 1:
#       tt = pair.index(all_pairs[j])
#       temp += all_pairs[j][0] + insert[tt]
#     else:

#       tt = pair.index(all_pairs[j])
#       temp += all_pairs[j][0] + insert[tt] + all_pairs[j][1]
#   print(i)
#   current = temp

# # print(len(current))
# print(current.count(max(set(current), key = current.count)) - current.count(min(set(current), key = current.count)))


# # NBBBCNCCNBBNBNBBCHBBHHBCHB
# # NBBBCNCCNBBNBNBBCHBHHBCHB
# # NBBBCNCCNBBNBNBBCHBHHBCHB

# # print("NBCCNBBBCBHCB" == "NBCCNBBBCBHCB")