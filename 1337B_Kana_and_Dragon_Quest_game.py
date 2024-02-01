noTests = int(input())

for i in range(noTests):
  parameters = input()
  parameters = parameters.split(" ")
  for el in parameters:
    dragonsHitPoints = int(parameters[0])
    noVoidAbsorptions = int(parameters[1])
    noLightningStrikes = int(parameters[2])

  while noVoidAbsorptions > 0:
    if dragonsHitPoints <= 10:
      break
    dragonsHitPoints = dragonsHitPoints // 2 + 10
    noVoidAbsorptions -= 1

  if dragonsHitPoints - 10 * noLightningStrikes <= 0:
    print("YES")
  else:
    print("NO")
