T = int(input())
for _ in range(T):
  numbers = list(map(int, input().split()))
  even_num = []
  for i in range(len(numbers)):
    if numbers[i]%2 == 0:
      even_num.append(numbers[i])
  print(sum(even_num), min(even_num))