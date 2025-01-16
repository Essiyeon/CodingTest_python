T = int(input())
arr = []

for _ in range(T):
    arr = input().split()
    for i in range(1,len(arr)):
        arr[0] = float(arr[0])
        if arr[i] == '@':
            arr[0] *= 3
        elif arr[i] == '%':
            arr[0] += 5
        elif arr[i] == '#':
            arr[0] -= 7
    print(f"{arr[0]:.2f}")