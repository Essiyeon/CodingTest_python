import sys

n,m = map(int, sys.stdin.readline().split()) # 도감에 수록된 포켓몬, 문제 개수
num_to_name = {}
name_to_num = {}

for i in range(1,n+1):
  name = sys.stdin.readline().strip()
  num_to_name[i] = name # (1:Bulbasaur)
  name_to_num[name] = i # (Bulbasaur:1)

for _ in range(m):
  a = sys.stdin.readline().strip()
  if a.isdigit():
    print(num_to_name[int(a)])
  else:
    print(name_to_num[a])
  