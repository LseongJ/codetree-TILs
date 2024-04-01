word = input()
cnt = 1
result = ""

for i in range(len(word)):
    # 첫 번째 문자일 경우
    if i == 0:
        continue

    # 현재 문자와 이전 문자가 다를 경우
    if word[i] != word[i - 1]:
        result += word[i - 1] + str(cnt)
        cnt = 1
    else:
        cnt += 1

# 마지막 문자열 처리
result += word[-1] + str(cnt)

# 결과 출력
print(len(result))
print(result)