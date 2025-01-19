K, N, M = map(int, input().split())
money = 0
if M - (K * N) < 0:
    money = -(M - (K * N))
else:
    money = 0
print(money)