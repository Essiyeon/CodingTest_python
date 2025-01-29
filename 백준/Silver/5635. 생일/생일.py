n = int(input())
student = []

for _ in range(n):
  data = input().split()
  name = data[0]
  day, month, year = map(int,data[1:])
  student.append((year, month, day, name))

student.sort()
print(student[-1][3])
print(student[0][3])
  