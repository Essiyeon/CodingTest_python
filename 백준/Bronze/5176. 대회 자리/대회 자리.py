K = int(input())
for _ in range(K):
  want = []
  P, M = map(int, input().split())
  for _ in range(P):
    want.append(int(input()))
  print(len(want)-len(set(want)))