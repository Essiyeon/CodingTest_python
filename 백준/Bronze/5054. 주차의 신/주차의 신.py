t = int(input())
for _ in range(t):
  n = int(input())
  store = list(map(int, input().split()))
  store = sorted(store)
  walk = 0
  for i in range(1, len(store)):
    walk += store[i] - store[i-1]
  print(walk*2)
  
  