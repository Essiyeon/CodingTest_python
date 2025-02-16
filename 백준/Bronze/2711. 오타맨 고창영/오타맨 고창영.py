T = int(input())
for _ in range(T):
  where, string = input().split()
  where = int(where)
  print(string[0:where-1]+string[where:])