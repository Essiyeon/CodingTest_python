N = int(input())
Iscute = []

for _ in range(N):
    Iscute.append(int(input()))

if Iscute.count(0) > Iscute.count(1):
    print('Junhee is not cute!')
else: print('Junhee is cute!')