n = int(input())
preq = 1
for i in range(n):
  for j in range(1, n+1):
    print(j * preq, end=" ")
  preq += 1
  print()