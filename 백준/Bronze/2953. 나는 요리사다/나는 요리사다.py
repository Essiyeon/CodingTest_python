sum_list = []
for _ in range(5):
  score = input().split()
  for i in range(len(score)):
    score[i] = int(score[i])
  sum_list.append(sum(score))

max_score = max(sum_list)
winner = sum_list.index(max_score)+1
print(winner, max_score)