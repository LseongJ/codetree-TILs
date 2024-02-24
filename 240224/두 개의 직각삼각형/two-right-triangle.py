n = int(input())

# 별의 개수 8 6 4 2
# 공백 개수 0 2 4 6 -> 2i

# n개의 별 출력 -> n-4 공백 출력 -> * n개의 별 출력
# n-1개 별 -> n-2 공백 -> n-1개별
# n-2개 별 -> n 공백 -> n-2개별
# n-3개 별 -> n+2 공백 -> n-3개별

# j = 4, 3, 2, 1 (i == 0)
# j = 3, 2, 1 (i == 1)
# j = 2, 1 (i == 2)
# j = 1 (i == 3)

for i in range(n):
    for j in range(n - i):
        print("*", end="")
    print(" " * (2*i), end="")
    for j in range(n - i):
        print("*", end="")

        
        
        
        
            

    print()