import sys

n, m = map(int, sys.stdin.readline().split())
not_hear = set()
not_see = set()

for _ in range(n):
  not_hear.add(sys.stdin.readline().rstrip())
for _ in range(m):
  not_see.add(sys.stdin.readline().rstrip())

not_hear_not_see = not_hear & not_see
sorted_list = list(sorted(not_hear_not_see))
print(len(sorted_list))

for i in range(len(sorted_list)):
  print(sorted_list[i])
    


