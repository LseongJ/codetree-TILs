n = int(input())
arr = list(map(int, input().split()))
cnt_2 = 0
cnt_remove = 0
for i in range(n):
  if arr[0] == 2:
    cnt_2 += 1
  arr.remove(arr[0])
  cnt_remove += 1
  if cnt_2 == 3:
    break
print(cnt_remove)