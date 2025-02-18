T = int(input())
for _ in range(T):
  arr = []
  idx = 0
  n = int(input())
  while (n > 0):
    if n%2 == 1:
      arr.append(str(idx))
    idx += 1
    n = n//2
  print(' '.join(arr))