numbers = []
for _ in range(5):
  numbers.append(int(input()))

average = sum(numbers)//len(numbers)
print(average)
numbers = sorted(numbers)
print(numbers[2])