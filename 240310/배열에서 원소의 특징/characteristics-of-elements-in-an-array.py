arr = list(map(int,input().split()))
point = 0
for elem in arr:
  if elem % 3 == 0:
    point = arr.index(elem)

    
    break
print(arr[point-1])