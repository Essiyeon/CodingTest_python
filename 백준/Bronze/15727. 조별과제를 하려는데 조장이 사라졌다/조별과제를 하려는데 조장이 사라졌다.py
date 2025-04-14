l = int(input())

if l%5 != 0:
  t = (l//5)+1
elif l < 5:
  t = l%5
elif l%5 == 0:
  t = l//5

print(t)