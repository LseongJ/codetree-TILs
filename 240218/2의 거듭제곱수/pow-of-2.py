n = int(input())
prod = 1
ans = 0
while True:
    prod *= 2
    ans += 1
    if (prod == n):
        print(ans)
        break