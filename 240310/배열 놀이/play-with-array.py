n, q = map(int, input().split())
n_elem = list(map(int, input().split()))

# q개의 질의응답
for _ in range(q):
  question =  list(map(int, input().split()))
  if question[0] == 1:
    print(n_elem[question[1] - 1])
  elif question[0] == 2:
    if question[1] in n_elem:
      print(n_elem.index(question[1]) + 1)
    else:
      print(0)
  elif question[0] == 3:
    for i in n_elem[question[1]-1:question[2]:1]:
      print(i, end=' ')