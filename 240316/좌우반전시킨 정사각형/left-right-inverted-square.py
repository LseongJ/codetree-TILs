n = int(input())
preq = 1
for i in range(n):
  for j in range(n, 0, -1):
    print(j * preq, end=" ")
  preq += 1
  print()