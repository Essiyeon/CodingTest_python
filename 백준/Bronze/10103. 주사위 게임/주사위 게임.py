n = int(input())
changyoung = 100
sangduck = 100

for _ in range(n):
  a,b = map(int,input().split()) # a=창영, b=상덕
  if a > b :
    sangduck -= a
  elif a < b :
    changyoung -= b
    
print(changyoung)
print(sangduck)
    
    
