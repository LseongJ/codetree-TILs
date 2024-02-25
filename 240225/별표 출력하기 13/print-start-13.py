# 홀수 행 -> 감소, 짝수 행 -> 증가
n = int(input())
cnt_even = 0
cnt_odd = n

for i in range(1, 2*n+1):
    if (i % 2 == 0):
        cnt_even += 1
        for k in range(cnt_even):
            print("*" , end=" ")
    else:
        for j in range(cnt_odd):
            print("*", end=" ")
        cnt_odd -= 1
    print()