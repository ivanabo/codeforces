noTests = int(input())

for i in range(noTests):
  args = input().split(" ")
  a = int(args[0])
  b = int(args[1])
  c = int(args[2])
  if (a<b and b<c):
    print("STAIR")
  elif (a<b and b>c):
    print("PEAK")
  else:
    print("NONE")