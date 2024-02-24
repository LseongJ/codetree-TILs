n = int(input())

for i in range(n, 0, -1):
    for k in range(n - i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()

for i in range(1, n):
    for j in range(n - i - 1):   # 공백 : 2 -> 1 -> 0
        print(" ", end=" ")
    for k in range(2*i + 1):
        print("*", end=" ")
    print()