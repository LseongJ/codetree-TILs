n = int(input())

for i in range(n, 0, -1):   # n번 반복
    for k in range(i):   # n번 반복
        for j in range(i):   # n번 반복
            print("*", end="")  # i = 4 ****
        print(" ",end="")    
    print()