word = list(map(str, input()))
gather = ['a', 'e', 'i', 'o', 'u']
count = 0
for char in word:
  if char in gather:
    count += 1
print(count)