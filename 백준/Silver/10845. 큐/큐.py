import sys
n = int(sys.stdin.readline())
que = []

for _ in range(n):
  order = list(map(str,sys.stdin.readline().split()))
  # print(order)
  if order[0] == 'push':
    que.append(int(order[1]))
    # print(que)
  elif order[0] == 'pop':
    if len(que) == 0:
      print(-1)
    else:
      print(que[0])
      que.remove(que[0])
  elif order[0] == 'size':
    print(len(que))
  elif order[0] == 'empty':
    if len(que) == 0:
      print(1) # 비어있음
    else:
      print(0) # 비어있지 않음
      # print(que)
  elif order[0] == 'front':
    if len(que) == 0:
      print(-1)
    else:
      print(que[0])
  elif order[0] == 'back':
    if len(que) == 0:
      print(-1)
    else:
      print(que[-1])