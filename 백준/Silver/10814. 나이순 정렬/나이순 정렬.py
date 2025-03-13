N = int(input())
members = []

for i in range(N):
  age, name = input().split()
  age = int(age)
  members.append((age,name,i))

def sort_key(item):
  return (item[0], item[2])

sorted_members = sorted(members, key=sort_key)

for age, name, _ in sorted_members:
  print(age, name)