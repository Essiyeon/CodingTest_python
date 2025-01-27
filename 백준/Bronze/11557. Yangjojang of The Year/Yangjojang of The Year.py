T = int(input())

for _ in range(T):
  N = int(input())
  data = {}
  for _ in range(N):
    S, L = input().split()
    L = int(L)
    data[S] = L
  # print(data)
  max_key = max(data, key=data.get)
  print(max_key)
    
    
