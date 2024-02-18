n = int(input())
ans = False

for i in range(2, n):
    if (n % i == 0):
        ans = True
        print("C")
        break
    else:
        print("P")
        break