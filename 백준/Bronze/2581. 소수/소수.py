M = int(input())
N = int(input())
sosu = []

for i in range(M,N+1):
  for j in range(2,i+1):
    if i%j == 0 :
      if i == j :
        sosu.append(i)
      break;

if len(sosu) == 0:
  print(-1)
else:
  print(sum(sosu))
  print(min(sosu))
