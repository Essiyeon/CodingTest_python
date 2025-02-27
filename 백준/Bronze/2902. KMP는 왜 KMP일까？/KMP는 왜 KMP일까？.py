long_type = input()
short_type = ''
for char in long_type:
  if char.isupper() :
    short_type += char
print(short_type)