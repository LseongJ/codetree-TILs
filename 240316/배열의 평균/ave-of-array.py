arr = []
for _ in range(2):
  arr_1 = list(map(int, input().split()))
  arr.append(arr_1)

# 가로 평균
sum_row = 0
for i in range(2):
  for j in range(len(arr[i])):
    sum_row += arr[i][j]
  print(f"{sum_row / 4:.1f}", end=" ")
  sum_row = 0
print()

# 세로 평균
sum_col = 0
for i in range(4):
  for j in range(2):
    sum_col += arr[j][i]
  print(f"{sum_col / 2:.1f}", end=" ")
  sum_col = 0
print()

# 전체 평균
sum1 = sum(arr[0])
sum2 = sum(arr[1])
ans = (sum1 + sum2) / 8
print(f"{ans:.1f}")