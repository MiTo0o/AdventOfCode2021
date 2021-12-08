# with open('input/d8.txt') as f:
#   data = [line.strip().split(" | ") for line in f]
#   data = [[i[0].split(), i[1].split()] for i in data]
  
#   c = 0
#   for i in data:
#     x = i[1]
#     print(x)
#     for j in x:
#       if len(j) == 2 or len(j) == 3 or len(j) == 7 or len(j) == 4:
#         c += 1
#   print(c)
with open('input/d8.txt') as f:
  data = [line.strip().split(" | ") for line in f]
  data = [[i[0].split(), i[1].split()] for i in data]
  
  c = 0
  for i in data:
    m = {
      "0":"", "1":"", "2":"", "3":"", "4":"", "5":"", "6":"", "7":"", "8":"", "9":""
    }
    x = i[0]
    for j in x:
      if len(j) == 2:
        m["1"] = j
      elif len(j) == 3:
        m["7"] = j
      elif len(j) == 7:
        m["8"] = j
      elif len(j) == 4:
        m["4"] = j
    for j in x:
      if len(j) == 6 and (j.count(m["1"][0]) == 1 and j.count(m["1"][1]) == 0 or j.count(m["1"][0]) == 0 and j.count(m["1"][1]) == 1):
        m["6"] = j
    for j in x:
      if len(j) == 5 and (j.count(m["1"][0]) == 1 and j.count(m["1"][1]) == 1):
        m["3"] = j
    tr = ""
    br = ""
    t = ""
    b = ""
    mid = ""
    bl = ""
    tl = ""
    for j in x:
      if len(j) == 5:
        t = [i for i in j if i not in m["6"]]
        if t != []:
          tr = t[0]
          br = [i for i in m["1"] if i != tr][0]
          break
    for j in x:
      if len(j) == 3:
        t = [i for i in j if i not in m["1"]][0]
    b = [i for i in m["3"] if i not in m["4"]+t][0]
    mid = [i for i in m["3"] if i not in tr+br+t+b ][0]
    tl = [i for i in m["4"] if i not in mid+tr+br ][0]
    bl = [i for i in m["8"] if i not in tr+br+t+b+mid+tl ][0]
    for j in x:
      if len(j) == 6:
        if "".join(sorted(j)) == "".join(sorted(tr+br+t+b+tl+bl)):
          m["0"] = j
        elif "".join(sorted(j)) == "".join(sorted(t+tl+tr+mid+b+br)):
          m["9"] = j
      elif len(j) == 5:
        if "".join(sorted(j)) == "".join(sorted(t+tl+mid+br+b)):
          m["5"] = j
        elif "".join(sorted(j)) == "".join(sorted(t+tr+mid+bl+b)):
          m["2"] = j

    boi = {}
    for k,v in m.items():
      boi[k] = "".join(sorted(v))
    xd = i[1]
    num = ""
    # print(b)
    # print(boi)
    for i in xd:
      s = "".join(sorted(i))
      # print(s)
      for k, v in boi.items():
        if v == s:
          # print(k)
          num += k

    # print(num)
    c += int(num)
    # print(num)
    # c += int(num)
    # print(xd)
    # print(tr,br,t,b,mid,tl,tr)
    # print(b)
    # for j in x:
    #   if len(j) == 6 and :
    #     m["9"] = j
  # print(c)
  # for i in data:
  #   print(i)
  print(c)
  
  
# fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
# aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
# fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
# dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
# bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
# egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
# gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce