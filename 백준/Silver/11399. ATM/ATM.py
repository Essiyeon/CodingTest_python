n = int(input())

p = list(map(int, input().split()))
#[3,1,4,3,2] 걸리는 시간
#[2,5,1,4,3] 줄 서는 순서
# 총 걸린 시간 (최소) : 32

# print(p)
# print(p.sort())
# print(1+1+2+1+2+3+1+2+3+3+1+2+3+3+4)
p.sort()
total = 0
for i in range(len(p)):
  for j in range(i+1):
      total += p[j]
print(total)





