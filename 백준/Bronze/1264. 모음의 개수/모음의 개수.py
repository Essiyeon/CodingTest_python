vowel = ['a', 'e', 'i', 'o', 'u']

while True:
  count = 0
  input_s = input()
  input_s = input_s.lower()
  
  if input_s == '#':
    break;

  for s in input_s:
    if s in vowel:
      count += 1

  print(count)
  