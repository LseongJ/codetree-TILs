n = int(input())
n_pass = 0 
mean = 0
for i in range(n):
  score = list(map(int,input().split()))
  for elem in score:
    mean += elem / len(score)
  if mean >= 60:
    n_pass += 1
    print('pass')
    mean = 0
  else:
    print('fail')
    mean = 0  
print(n_pass)