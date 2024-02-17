p1, g1 = input().split()
p2, g2 = input().split()

if ((int(p1) >= 19 and g1 == 'M') or (int(p2) >= 19 and g2 == "M")):
    print(1)
else:
    print(0)