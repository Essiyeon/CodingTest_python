T = int(input())
for _ in range(T):
  N = int(input())
  number = input().split()

  for i in range(len(number)):
    number[i] = int(number[i])

  print(sum(number))