N, K = map(int, input().split())
A = []
coin = 0

for _ in range(N):
  A.append(int(input()))

A.sort(reverse = True)
for a in A:
  if a < K or a == K:
    coin += K//a
    K = K%a

print(coin)