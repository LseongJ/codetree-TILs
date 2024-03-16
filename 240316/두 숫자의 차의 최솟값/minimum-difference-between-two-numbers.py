import sys
n = int(input())
arr = list(map(int,input().split()))
minus_arr = []
for i in range(n):
  for j in range(1, n):
    differ = arr[i] - arr[j]
    if differ < 0:
      differ *= -1
    minus_arr.append(differ)
    if differ == 0:
      minus_arr.remove(differ)




min_value = sys.maxsize

for k in range(n):
  if minus_arr[k] < min_value:
    min_value = minus_arr[k]
    
print(min_value)


# 5
# 3 6 7 10 43