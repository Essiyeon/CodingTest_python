T = int(input())

for _ in range(T):
  sound = input().split()

  while True:
    animal = input().split()
    if animal[-1] =='say?':
      break
    sound = list(filter(lambda x: x != animal[2],sound))
      
  print(' '.join(sound))