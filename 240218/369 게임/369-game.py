n = int(input())

for i in range(1, n+1):

    if (i == 1 or i == 2):
        print(i, end=" ")

    elif (3 <= i < 10):
        if (i % 3 == 0):
            print(0, end=' ')
        else:
            print(i, end=" ")
    
    elif (i >= 10):
        if (i % 3 == 0):
            print(0, end=" ")
        else:
            print(i, end=" ")





        # 13 % 3 = 1
        # 23 % 3 = 2
        # 33 % 3 = 0

        # 31 // 10 = 3