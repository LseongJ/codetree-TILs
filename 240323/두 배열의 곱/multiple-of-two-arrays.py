arr1 = [
      list(map(int, input().split()))
      for _ in range(3)
]

arr2 = [
      list(map(int, input().split()))
      for _ in range(3)
]

arr_ans = [
    [ 0 for _ in range(3)]
    for _ in range(3)
]

for i in range(3):
  for j in range(3):
    arr_ans[i][j] = arr1[i][j] + arr2[i][j]
    print(arr_ans[i][j], end = " ")
  print()