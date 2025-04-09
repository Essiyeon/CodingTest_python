n = int(input())

for _ in range(n):
  s = int(input())
  
  x = 2
  while x <= 1000000 :
    if s%x == 0:
        print("NO")
        break
    x += 1
  else:
    print("YES")