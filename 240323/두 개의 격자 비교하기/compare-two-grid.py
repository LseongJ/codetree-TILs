row, col = map(int, input().split())
arr1 = [
    list(map(int, input().split()))
    for _ in range(row)
]
arr2 = [
    list(map(int, input().split()))
    for _ in range(row)
]

ans = [
    [0 for _ in range(col)]
    for _ in range(row)
]
for i in range(row):
  for j in range(col):
    if arr1[i][j] != arr2[i][j]:
      ans[i][j] = 1

for row in ans:  # 수정: 각 행을 한 줄에 출력
    for elem in row:
        print(elem, end=" ")
    print()