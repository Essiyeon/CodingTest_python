string = str(input())
string_list = list(string)
reverse_string = ''
for s in string_list:
  if s.isupper() == True:
    s = s.lower()
    reverse_string += s
  else:
    s = s.upper()
    reverse_string += s
print(reverse_string)