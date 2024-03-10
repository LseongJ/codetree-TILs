n1, n2 = map(int, input().split())
arr = []
ans = []
ans.append(n1)
ans.append(n2)

for i in range(2, 10):
  ans.append(ans[i-1] + 2*ans[i-2])

for elem in ans:
  print(elem, end=' ')