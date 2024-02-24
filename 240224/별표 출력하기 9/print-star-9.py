n = int(input())


for i in range(n):  # escape
    for j in range(n - i, 1, -1):
        print(" ", end=" ")
    for k in range(2*i + 1):
        print("*", end=" ")
            
    print()