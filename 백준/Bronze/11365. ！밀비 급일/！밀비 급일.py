while True:
  s = input()
  decode = ''
  
  if s == 'END':
    break

  for i in range(len(s)-1,-1,-1):
    decode += s[i]

  print(decode)