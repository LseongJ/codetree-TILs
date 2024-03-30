n, m = map(int, input().split())

grid_ = [ [0] * n for _ in range(n)]

for i in range(m):
  x, y = tuple(map(int, input().split()))
  grid_[x-1][y-1] = x * y

for row in grid_:
  for elem in row:
    print(elem, end=" ")
  print()