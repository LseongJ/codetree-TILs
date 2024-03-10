n = int(input())
arr = list(map(int,input().split()))

revenge_arr = arr[::-1]
for elem in revenge_arr:
  if elem % 2 == 0:
    print(elem, end=" ")