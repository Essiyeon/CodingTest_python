import sys

n, m = map(int, sys.stdin.readline().split())
not_hear = []
not_see = []
count = 0

for _ in range(n):
  not_hear.append(sys.stdin.readline().rstrip())
set_not_hear = set(not_hear)
for _ in range(m):
  not_see.append(sys.stdin.readline().rstrip())
set_not_see = set(not_see)

not_hear_see = []

for h in set_not_hear:
  if h in set_not_see:
    not_hear_see.append(h)
    count += 1

print(count)
not_hear_see.sort()
for i in range(len(not_hear_see)):
  print(not_hear_see[i])
    


