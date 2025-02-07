T = int(input())
for _ in range(T):
  V, E = map(int, input().split()) # 꼭짓점V, 모서리E
  M = 2-V+E
  print(M)  