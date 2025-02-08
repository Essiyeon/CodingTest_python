n = int(input())
star = '* '

for i in range(n-1,0,-1):
    print(' '*i + star*(n-i))

print(star*n)