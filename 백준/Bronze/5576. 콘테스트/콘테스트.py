score = []
for _ in range(20):
  score.append(int(input()))
  
W_score = score[:10]
K_score = score[10:]
W_score.sort(reverse=True)
K_score.sort(reverse=True)

W_max = 0
K_max = 0

for i in range(3):
  W_max += W_score[i]
  K_max += K_score[i]

print(W_max, K_max)
