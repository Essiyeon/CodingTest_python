n = int(input())

for i in range(1,n):
  digit_sum = sum(map(int, str(i)))
  if i + digit_sum == n:
    print(i)
    break
else:
  print(0)