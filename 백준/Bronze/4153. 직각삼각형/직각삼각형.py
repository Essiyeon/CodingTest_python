while True:
  # a, b, c = map(int, input().split())
  numbers = list(map(int, input().split()))
  
  if numbers.count(0) == 3 :
    break

  c = max(numbers)
  numbers.remove(c)
  a = numbers[0]
  b = numbers[1]
  
  if a*a + b*b == c*c:
    print('right')
  else:
    print('wrong')