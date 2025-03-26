t = int(input())
for _ in range(t):
  h, w, n = map(int, input().split()) #층 수, 방 수, 몇 번째 손님인지
  y = (n%h) # 층 수
  if y == 0:
    x = (n//h)
    y = str(h)
  else:
    x = (n//h)+1 # 호 수
  if x < 10 :
    x = '0' + str(x)
  print(str(y)+str(x))
