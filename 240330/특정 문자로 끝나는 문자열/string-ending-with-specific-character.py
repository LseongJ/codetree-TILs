arr = [0] * 10

for _ in range(10):
  arr[_] = input()

key = input()
cnt = 0

for i in range(10):
  if arr[i][len(arr[i])-1] == key:
    cnt += 1
    print(arr[i])

if cnt == 0:
  print("None")