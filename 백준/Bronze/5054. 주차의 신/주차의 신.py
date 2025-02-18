t = int(input())
for _ in range(t):
  n = int(input())
  store = input().split()
  walk = 0
  for i in range(len(store)):
    store[i] = int(store[i])
  store = sorted(store)
  # print(store)
  for i in range(1, len(store)):
    walk += store[i] - store[i-1]
  print(walk*2)
  
  