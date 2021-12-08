with open('input/d8.txt') as f:
  data = [line.strip().split(" | ") for line in f]
  data = [[i[0].split(), i[1].split()] for i in data]
  
  c = 0
  for i in data:
    m = {str(i):"" for i in range(11)}
    x = i[0]
    
    for j in x:
      if len(j)   == 2: m["1"] = j
      elif len(j) == 3: m["7"] = j
      elif len(j) == 7: m["8"] = j
      elif len(j) == 4: m["4"] = j
      
    for j in x:
      if len(j) == 6 and (j.count(m["1"][0]) + j.count(m["1"][1]) == 1):
        m["6"] = j
      if len(j) == 5 and (j.count(m["1"][0]) + j.count(m["1"][1]) == 2):
        m["3"] = j

    tr  = [i for i in m["8"] if i not in m["6"]][0]
    br  = [i for i in m["1"] if i not in tr][0]
    t   = [i for i in m["7"] if i not in m["1"]][0]
    b   = [i for i in m["3"] if i not in m["4"]+t][0]
    mid = [i for i in m["3"] if i not in tr+br+t+b][0]
    tl  = [i for i in m["4"] if i not in mid+tr+br][0]
    bl  = [i for i in m["8"] if i not in tr+br+t+b+mid+tl][0]
    
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
          
    switched = {"".join(sorted(v)):k for k,v in m.items()}
    num = "".join([switched["".join(sorted(i))] for i in i[1]])
    c += int(num)
  print(c)