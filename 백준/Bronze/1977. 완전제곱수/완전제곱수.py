import math

M = int(input())
N = int(input())
perfect_squre_number = []

for i in range(M,N+1):
  a = math.isqrt(i)
  if a*a == i:
    perfect_squre_number.append(i)

if len(perfect_squre_number) == 0:
  print(-1)
else:
  print(sum(perfect_squre_number))
  print(min(perfect_squre_number))
  

