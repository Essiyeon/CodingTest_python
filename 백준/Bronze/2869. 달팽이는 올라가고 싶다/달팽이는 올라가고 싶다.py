a, b, v = map(int, input().split())
count = 0

days = (v - a) // (a - b)
if (v - a) % (a - b) == 0:
  print(days+1)
else:
  print(days+2)