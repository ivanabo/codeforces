noTests = int(input())

for i in range(noTests):
  args = input().split(":")
  h = int(args[0])
  m = int(args[1])
  if(0<=m and m<=9):
    mstr = '0'+str(m)
  else:
    mstr = str(m)
    
  if (0<h and h<12):
    if (0<=h and h<=9):
      hstr = '0'+str(h)
    else:
      hstr = str(h)
    print(hstr + ":" + mstr + " AM")
  elif h==12:
    hstr = str(h)
    print(hstr + ":" + mstr + " PM")
  elif h==0:
    hstr = str(h+12)
    print(hstr + ":" + mstr + " AM")
  else:
    h = h-12
    if (0<=h and h<=9):
      hstr = '0'+str(h)
    else:
      hstr = str(h)
    print(hstr + ":" + mstr + " PM")