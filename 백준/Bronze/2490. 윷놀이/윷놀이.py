for _ in range(3):
  yut = input().split()
  if yut.count('0') == 1:
    print("A") #도
  elif yut.count('0') == 2:
    print("B") #개
  elif yut.count('0') == 3:
    print("C") #걸
  elif yut.count('0') == 4:
    print("D") #윷
  else:
    print("E")