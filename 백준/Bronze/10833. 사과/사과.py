N = int(input())
remain = []
for _ in range(N):
  student, apple = map(int, input().split())
  remain.append(apple%student)

print(sum(remain))