import sys
input = sys.stdin.readline

N = int(input())
P = 0

for _ in range(N):
  P += int(input())
print(P-(N-1))