A, B = map(int,input().split())

list = []
num = 1
while len(list) < B:
  list.extend([num]*num)
  num += 1

print(sum(list[A-1:B]))