n = int(input())
result = 0

for i in range(1, n+2):
  if n < i:
    if i % 2 == 1: # i가 홀수이면 == 푸앙이 차례
        print(i - n)
    else:
        print(0)
    break
  n -= i