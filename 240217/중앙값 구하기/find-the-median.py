a, b, c = map(int, input().split())

if (a > b):
    if (b > c):
        print(b)
    else:
        if(a > c):
            print(c)
        else:
            print(a)

else:
    if(a < c):
        if (b < c):
            print(b)
        else:
            print(c)
    else:
        print(a)