n = int(input())
for _ in range(n):
  line = input()
  line_list = list(map(str, line))
  line_list[0] = line_list[0].upper()
  result = ''
  for i in range(len(line_list)):
    result += line_list[i]
  print(result)