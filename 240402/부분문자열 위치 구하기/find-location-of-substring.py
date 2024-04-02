word = input()
obj = input()

w = len(word)
o = len(obj)

exist = False

for i in range(w - o + 1):
    # 문자열 obj와 word[i:i+o]가 같은지 확인
    if word[i:i+o] == obj:
        exist = True
        print(i)  # 첫 번째로 등장하는 위치를 출력
        break

if exist = False:
    print(-1)