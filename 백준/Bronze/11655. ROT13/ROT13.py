S = input()
new_string = ''

for char in S:
  if 'A' <= char <= 'Z':
    new_string += chr((ord(char)-ord('A')+13) %26 +ord('A'))
  elif 'a' <= char <= 'z':
    new_string += chr((ord(char)-ord('a')+13) %26 +ord('a'))
  else:
    new_string += char
print(new_string)