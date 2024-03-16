import sys
n = int(input())
arr = list(map(int,input().split()))
minus_arr = []
for i in range(1, n):
  for j in range(n):
    abs = arr[i] - arr[j]
    if abs < 0:
      abs *= -1
    minus_arr.append(abs)



min_value = sys.maxsize

for k in range(n):
  if minus_arr[k] < min_value:
    if minus_arr[k] == 0:
      min_value += 0
    else:
      min_value = minus_arr[k]
print(min_value)


# 5
# 3 6 7 10 43