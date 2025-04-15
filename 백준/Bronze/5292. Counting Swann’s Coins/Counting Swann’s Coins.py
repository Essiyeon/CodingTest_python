num = int(input())
result = []

for i in range(1, num+1):
  if i%3 == 0 and i%5 != 0:
    if result:
      print(' '.join(result) + ' Dead')
    else:
      print('Dead')
    result = []
  elif i%5 == 0 and i%3 != 0:
    if result:
      print(' '.join(result) + ' Man')
    else:
      print('Man')
    result = []
  elif i%15 == 0:
    if result:
      print(' '.join(result) + ' DeadMan')
    else:
      print('DeadMan')
    result = []
  else:
    result.append(str(i))

if result:
  print(' '.join(result))