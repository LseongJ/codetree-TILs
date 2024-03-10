a, b = map(int, input().split())
count_arr = [0] * b
cal_arr = []
while a > 1:
  count_arr[a % b] += 1
 
  a //= b
 


ans = sum([i ** 2 for i in count_arr])
print(ans)