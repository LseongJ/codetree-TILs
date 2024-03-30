ans = []
for i in range(2):
    w = input()
    for j in w:
        if j != " ":
            ans.append(j)

for k in ans:
    print(k, end="")