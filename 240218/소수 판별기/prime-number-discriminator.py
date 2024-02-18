n = int(input())
ans = False

for i in range(2, n+1):
    if (n % i == 0):
        ans = True
        break
    else:
        break

if ans == True:
    print("C")
else:
    print("P")