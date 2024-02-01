line = input()

words = line.split("WUB")
for word in words:
  while ('WUB' in word):
    word.strip('WUB')

final = ""

for word in words:
  if word.isalpha():
    final += word + " "

print(final.strip(" "))
