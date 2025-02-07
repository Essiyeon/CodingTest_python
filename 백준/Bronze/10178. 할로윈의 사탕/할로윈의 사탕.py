T = int(input())
for _ in range(T):
  c, v = map(int, input().split())
  candy = c//v
  remain = c%v
  print(f'You get {candy} piece(s) and your dad gets {remain} piece(s).')