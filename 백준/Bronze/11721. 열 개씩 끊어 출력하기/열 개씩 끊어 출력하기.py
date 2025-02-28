N = input()
a = len(N)//10
b = len(N)%10
for i in range(0,a):
  print(N[10*i:10*i+10])
if b != 0:
  print(N[-b:])
