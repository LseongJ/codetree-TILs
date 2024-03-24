n = int(input())

ans = [[0] * n for _ in range(n)]

for _ in range(n):
  ans[0][_] = 1
  ans[_][0] = 1

for row in range(1, n):
  for col in range(1, n):
    ans[row][col] = ans[row][col-1] + ans[row-1][col] + ans[row-1][col-1]


for row in ans:
  for elem in row:
    print(elem, end=" ")
  print()