dot_x = []
dot_y = []

for _ in range(3):
    a,b = map(int, input().split())
    dot_x.append(a)
    dot_y.append(b)

unique_x = [x for x in dot_x if dot_x.count(x) == 1]
unique_y = [y for y in dot_y if dot_y.count(y) == 1]

print(unique_x[0], unique_y[0])