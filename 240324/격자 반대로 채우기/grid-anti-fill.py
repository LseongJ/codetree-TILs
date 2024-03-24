n = int(input())

ans = [[0] * n for _ in range(n)]
num = n ** 2

for col in range(n):
  if col % 2 == 0:
    for row in range(n-1, -1, -1):
      ans[row][col] = num
      num -= 1
  else:
    for row in range(n):
      ans[row][col] = num
      num -= 1

for row in ans:
  for elem in row:
    print(elem, end=" ")
  print()