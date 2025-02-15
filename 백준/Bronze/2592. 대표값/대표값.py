from collections import Counter
numbers = []

for _ in range(10):
  numbers.append(int(input()))

avg = int(sum(numbers)/len(numbers))
print(avg)

count_list = Counter(numbers).most_common()
print(count_list[0][0])