numbers = []
for _ in range(9):
  numbers.append(int(input()))

for i in range(len(numbers)):
  for j in range(i+1, len(numbers)):
    if sum(numbers) - numbers[i] - numbers[j] == 100:
      for k in range(len(numbers)):
        if k == i or k == j:
           pass
        else:
          print(numbers[k])