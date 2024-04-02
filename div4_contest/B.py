noTests = int(input())

for i in range(noTests):
  n = int(input())
  for j in range(n):
    str = ""
    if j%2 == 0:
      for k in range(n):
        if k%2 == 0:
          str += "##"
        else:
          str += ".."
      print(str)
      str = ""
      for k in range(n):
        if k%2 == 0:
          str += "##"
        else:
          str += ".."
      print(str)
    else:
      str = ""
      for k in range(n):
        if k%2 == 0:
          str += ".."
        else:
          str += "##"
      print(str)
      str = ""
      for k in range(n):
        if k%2 == 0:
          str += ".."
        else:
          str += "##"
      print(str)