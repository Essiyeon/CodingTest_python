x, y = map(str, input().split())

x_list = list(map(str, x))
x_list.reverse()
y_list = list(map(str, y))
y_list.reverse()

x_str = ''
y_str = ''
for a in x_list:
  x_str += a
# print(x_str)
for a in y_list:
  y_str += a
# print(y_str)

result = int(x_str)+int(y_str)
reverse_result = int(str(result)[::-1])
print(reverse_result)


  
