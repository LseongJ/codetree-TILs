import sys
n = int(input())
arr = list(map(int, input().split()))
ans = []
max_val = -sys.maxsize

while len(arr) > 0:
  for i in range(len(arr)):
    if arr[i] >= max_val:
      max_val = arr[i]
  
  ans.append(max_val)
  
  arr.remove(max_val)
  max_val = 0
  

print(ans[0], ans[1])