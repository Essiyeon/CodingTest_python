N = int(input())
result = input().split()
score = 0
count = 0

for i in range(len(result)):
  if result[i] == '1':
    count += 1
  else:
    count = 0
  score += count

print(score)