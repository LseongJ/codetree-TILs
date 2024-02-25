# i/j 0 1 2 3
# 0   * * * *
# 1   *     *  i == 1 j == 1, 2
# 2   * *   *  i == 2 j == 2
# 3   * * * *  

# 0 < i <= j 
n = int(input())

for i in range(n):
    for j in range(n):
        if (i == 0 or j == 0 or i == n-1 or j == n-1):
            print("*", end=" ")
        else:
            if(i > j):
                print("*",end=" ")
            else:
                print(" ",end=" ")

        
        
    print()