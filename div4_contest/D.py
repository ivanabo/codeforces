def checkBinary(n):
  flag = 1
  t = n
  while(t > 0):
    if(t%10 != 0 and t%10 != 1):
      flag = 0
      break
    else:
      t = t//10
  return flag

noTests = int(input())

for i in range(noTests):
  n = int(input())
  t = n
  if (checkBinary(n)):
    print("YES")
  else:
    b = 0
    while(t>10):
      if(t%11 == 0):
        if(checkBinary(t//11)):
          print("YES")
          b = 1
          break
        else:
          t = t//11
      if(t%100 == 0):
        if(checkBinary(t//100)):
          print("YES")
          b = 1
          break
        else:
          t = t//100
      if(t%101 == 0):
        if(checkBinary(t//101)):
          print("YES")
          b = 1
          break
        else:
          t = t//101
      if(t%110 == 0):
        if (checkBinary(t//110)):
          print("YES")
          b = 1
          break
        else:
          t = t//110
      if(t%111 == 0):
        if(checkBinary(t//111)):
          print("YES")
          b = 1
          break
        else:
          t = t//111
      if(t%11!=0 and t%100!=0 and t%101!=0 and t%110!=0 and t%111!=0):
        break
        
    if(b==0):
      print("NO")