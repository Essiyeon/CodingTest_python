T = int(input())
y_score, k_score = 0, 0

for _ in range(T):
  for _ in range(9):
    Y, K = map(int,input().split())
    y_score += Y
    k_score += K

  if y_score > k_score :
    print("Yonsei")
  elif y_score < k_score :
    print("Korea")
  else: 
    print("Draw")
    
