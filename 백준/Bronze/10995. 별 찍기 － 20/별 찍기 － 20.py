n = int(input())
star = '* '
star_reverse = ' *'

for i in range(1,n+1):
  if i%2 != 0 :
    print(star*n)
  else:
    print(star_reverse*n)