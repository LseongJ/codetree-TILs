n = int(input())
cnt1 = 0
cnt2 = n

for i in range(1, 2*n+1): # 1 2 3 4 5 6
    if (i % 2 != 0):  # 홀수 행(i == 1 3 5)
        cnt1 += 1
        for j in range(cnt1): # 1 2 3
            print("*", end=" ")
    else:
        for k in range(cnt2):
            print("*", end=" ")
        cnt2 -= 1
    print()