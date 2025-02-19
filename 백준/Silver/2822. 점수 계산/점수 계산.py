score = []
idx = []
total = 0

for _ in range(8):
  score.append(int(input()))

for _ in range(5):
  max_score = max(score)
  total += max_score
  idx.append(score.index(max_score)+1)
  score[score.index(max_score)] = 0

print(total)
idx = sorted(idx)
print(' '.join(map(str,idx)))