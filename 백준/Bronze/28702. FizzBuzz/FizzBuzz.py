values = []
idx = 0
num = 0

for _ in range(3):
  values.append(input())

for i in range(len(values)):
  if values[i].isdigit():
    num = int(values[i])
    idx = i
    break
    
if idx == 2:
  num = num+1
elif idx == 1:
  num = num+2
else:
  num = num+3

if num%3 == 0 and num%5 == 0:
  print("FizzBuzz")
elif num%3 == 0 and num%5 !=0:
  print("Fizz")
elif num%3 != 0 and num%5 == 0:
  print("Buzz")
else:
  print(num)
  
