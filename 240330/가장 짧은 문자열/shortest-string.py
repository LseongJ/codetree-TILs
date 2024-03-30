w = [0] * 3
for i in range(3):
  w[i] = len(input())
print(max(w) - min(w))