N = int(input())

for _ in range(N):
    r, e, c = map(int,input().split())
    #광고안함, 광고함, 광고비용
    if r < e - c :
        print('advertise')
    elif r > e - c :
        print('do not advertise')
    else:
        print('does not matter')