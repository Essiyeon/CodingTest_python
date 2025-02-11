number = []
odd = []

for _ in range(7):
  number.append(int(input()))

for i in range(len(number)):
  if number[i]%2 != 0 :
    odd.append(number[i])

if len(odd) == 0:
  print(-1)
else:
  print(sum(odd))
  print(min(odd))