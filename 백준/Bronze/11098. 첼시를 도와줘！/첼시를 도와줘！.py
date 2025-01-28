n = int(input())
for _ in range(n):
  p = int(input()) # 고려해야될 선수 수
  player = {}
  for _ in range(p):
    C, name = input().split()
    C = int(C)
    player[name] = C
  max_key = max(player, key=player.get)
  print(max_key)
    
