T = int(input())

for _ in range (T):
  N = int(input())
  hakjum = []
  grade = []
  multi = []
  
  for _ in range(N):
    C, G = map(float, input().split())
    hakjum.append(int(C))
    grade.append(G)
    
  for i in range(N):
    multi.append(hakjum[i]*grade[i])
  GPA = sum(multi)/sum(hakjum)
  
  print(sum(hakjum),f'{GPA:.1f}')