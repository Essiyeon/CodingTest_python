T = int(input())
result = []

for _ in range(T):
  x, y = input().split()
  distances = []
  dist = 0
  for i in range(len(x)):
    if y[i] >= x[i]:
      dist = (ord(y[i]) - ord(x[i]))
    else:
      dist = (ord(y[i]) - ord(x[i]) +26)
    distances.append(str(dist))
  print('Distances:', ' '.join(distances))
