n, q = map(int, input().split())
n_elem = list(map(int, input().split()))

for i in range(q): # 질의 q회 반복
  quest = list(map(int, input().split()))
  
  if quest[0] == 1:
    print(n_elem[quest[1] - 1])   # 1 a > a번째 원소를 출력

  elif quest[0] == 2:
    if quest[1] in n_elem:
      print(n_elem.index(quest[1]) + 1)
    else:
      print(0)

  elif quest[0] == 3:
    for k in n_elem[quest[1] - 1 : quest[2]]:
      print(k, end = " ")