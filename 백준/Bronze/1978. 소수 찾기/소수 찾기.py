n = int(input())
is_sosu = list(map(int,input().split()))
sosu = []

for num in is_sosu:
  list = []
  for i in range(1,num+1):
    if num%i == 0 :
      list.append(i)
  if len(list) == 2:
    sosu.append(num)

print(len(sosu))
  