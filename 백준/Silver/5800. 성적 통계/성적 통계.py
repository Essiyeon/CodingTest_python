K = int(input())
for i in range(1, K+1):
  score = list(map(int, input().split()))
  score.remove(score[0])
  score.sort(reverse = True)
  # print(score)

  Largest_gap = 0
  for j in range(len(score)-1):
    if score[j] - score[j+1] > Largest_gap :
      Largest_gap = score[j] - score[j+1]
      
  print('Class', i)
  print(f'Max {max(score)}, Min {min(score)}, Largest gap {Largest_gap}')