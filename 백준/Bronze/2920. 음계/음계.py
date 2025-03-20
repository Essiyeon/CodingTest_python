input_num = list(map(int, input().split()))

if input_num == list(range(1, 9)):
    print("ascending")
elif input_num == list(range(8, 0, -1)):
    print("descending")
else:
    print("mixed")
