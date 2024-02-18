sum_ = 0
p = 0

while True:
    age = int(input())
    if (20 <= age <= 29):
        sum_ += age
        p += 1
    else:
        ans = sum_ / p
        break

print(f"{ans:.2f}")