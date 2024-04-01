n = int(input())
arr = list(map(str, input().split()))
cnt = 0
#모든 문자열 붙이기
word = ''.join(arr)

for i in word:
    print(i, sep='', end='')
    cnt += 1
    if cnt >= 5:
        print()
        cnt = 0